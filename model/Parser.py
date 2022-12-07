from dataclasses import dataclass
from typing import Any, List, Tuple
import re
from sqlite3 import Connection, Cursor
from pathlib import Path


WORD_SEARCH = "SELECT word,num,type FROM LEXICON WHERE word LIKE '{word}%'"
RELATION_SEARCH = """SELECT relation FROM RELATIONS
WHERE (first LIKE '%{first}%') and (second LIKE '%{second}%')"""


@dataclass
class Database:
    """Class for data."""

    conn: Connection
    curr: Cursor

    def __init__(self, file_name: str):
        # Make folder if not exists
        __match = re.search("([\\/]([\\w\\s]+[\\.][a-z]+)$)", file_name)
        if __match is not None:
            _path = file_name[0: __match.start() + 1]
            Path(_path).mkdir(parents=True, exist_ok=True)
        # Connect the database
        self.conn = Connection(file_name)
        self.curr = self.conn.cursor()

    def init(self, table_name: str = "FLIGHT"):
        """Init database with default requirements"""
        fp = open("./input/database.sql", encoding="utf-8")
        self.curr.executescript(fp.read())
        self.conn.commit()

    def close(self):
        self.conn.commit()
        self.curr.close()
        self.conn.close()


def lookup(word: str, db: Database):
    db.curr.execute(WORD_SEARCH.format(word=word))
    retVal = db.curr.fetchall()
    return retVal


def find_relation(
    first: str, second: str, db: Database,
    nsubj: bool = False, dobj: bool = False
) -> str:
    relation: str = "TBD"
    db.curr.execute(RELATION_SEARCH.format(first=first, second=second))
    res = db.curr.fetchall()
    if len(res) == 0:
        pass
    elif (res[0][0] == "nsubj") and (nsubj):
        if (res[1][0] == "dobj") and (dobj):
            relation = res[1][0]
        else:
            relation = res[2][0]
    else:
        # (relation,)
        relation = (res[0])[0]
    return relation


def analysis(words: List[str], db: Database) -> List[Tuple[str, str]]:
    retLst: List[Tuple[str, str]] = []
    i: int = 0
    L: int = len(words)
    while i < L:
        # Get the list of matching words
        lexicons = lookup(words[i].lower(), db)
        # Proceed item by item
        found: int = 0
        # Flag for not found
        if len(lexicons) == 0:
            retLst.append((f"{words[i]}", "TBD"))
            i += 1
            continue
        # In case of found in Database
        while len(lexicons) > 0:
            # lexicon = word | number of words | type of word
            lexicon = lexicons.pop()
            word = lexicon[0]
            num = lexicon[1]
            wType = lexicon[2]
            jword: str = ""
            for j in range(num):
                jword += f" {words[i+j]}"
            if (jword.strip().lower() == word) and (found < num):
                # Check if get the other value will pop it
                if found > 0:
                    retLst.pop()
                retLst.append((word, wType))
                found = num
        i += found
        continue
    return retLst


@dataclass
class Node:
    """The input is the data with Tuple(data, type)"""

    data: str
    type: str
    children: List[Any]
    length: int
    parent: Any
    relation: str

    def __init__(self, data: Tuple[str, str]) -> None:
        self.data = data[0]
        self.type = data[1]
        self.children = []
        self.length = 0
        self.relation = "TBD"
        self.parent = None

    def add_child(self, child, relation) -> None:
        child.update_parent(self, relation)
        self.children.append(child)
        self.length += 1
        return

    def update_parent(self, parent, relation) -> None:
        self.parent = parent
        self.relation = relation
        return

    def buildTree(self) -> str:
        xfactor = ""
        for child in self.children:
            xfactor += f"{child.buildTree()}\n\t"
        if xfactor == "":
            return f"({self.relation} ({self.data}))"
        elif self.relation == "TBD":
            return f"({self.data} ({xfactor}))"
        else:
            # return f"({self.relation} ({self.data}))"
            return f"({self.relation} ({self.data} ({xfactor})))"


@dataclass
class Parser:
    text: str
    root: Node
    __db__: Database
    __nsubj__: bool
    __dobj__: bool
    __buffer__: List[Node]
    __stack__: List[Node]
    __nSkip__: int

    def __init__(self, text: str, db: Database):
        self.text = text
        self.root = Node(("ROOT", "ROOT"))
        self.__buffer__ = []
        self.__db__ = db
        self.__nSkip__ = 0
        self.__dobj__ = False
        self.__nsubj__ = False
        __words = analysis(text.split(), self.__db__)
        for e in __words:
            self.__buffer__.append(Node(e))
        self.__buffer__.reverse()
        self.__stack__ = [self.root]

    def getTopStack(self):
        retNode: Node = Node(("null", "nulll"))
        try:
            retNode = self.__stack__[-1]
        except IndexError:
            pass
        return retNode

    def getTopBuffr(self):
        retNode: Node = Node(("null", "nulll"))
        try:
            retNode = self.__buffer__[-1]
        except IndexError:
            pass
        return retNode

    def RA(self, relation: str):
        # RA: This happens when the input element in buffer
        # has relation with the top element in stack
        topStack = self.getTopStack()
        topBuffer = self.getTopBuffr()
        # 1. Shift the input item to stack
        self.shift()
        # 2. Add the relation
        topStack.add_child(topBuffer, relation)
        # 3. Reduce if not verb and not any relation with the next input
        nextInput = self.getTopBuffr()
        if topBuffer.type == "VERB":  # Is it VERB?
            # self.root.add_child(topBuffer, relation)
            pass
        elif (
            find_relation(
                topBuffer.type,
                nextInput.type,
                self.__db__,
                self.__nsubj__,
                self.__dobj__,
            )
            != "TBD"
        ):  # Any relationship?
            self.__nSkip__ += 1
        else:  # Reduce
            self.reduce()
            while self.__nSkip__ > 0:
                self.reduce()
                self.__nSkip__ -= 1
        # RA is DONE !?
        return

    def LA(self, relation: str):
        # LA: This happens when the element on top of stack
        # has relation with buffer
        topStack = self.getTopStack()
        topBuffer = self.getTopBuffr()
        if topStack.type == "VERB":
            pass
        else:
            self.reduce()
        topBuffer.add_child(topStack, relation)
        # LA is DONE !?
        return

    def reduce(self):
        try:
            self.__stack__.pop()
        except IndexError:
            print("Warning: Empty stack!!!")
            pass

    def shift(self) -> Node:
        __tmp: Node = Node(("null", "null"))
        try:
            __tmp = self.__buffer__.pop()
            self.__stack__.append(__tmp)
        except IndexError:
            print("Warning: Empty stack!!!")
            pass
        return __tmp

    def do_MaltParser(self):
        while len(self.__buffer__) > 0:
            topStack: Node = self.getTopStack()
            topBuff: Node = self.getTopBuffr()
            # check for the relation
            resRA = find_relation(
                topStack.type, topBuff.type, self.__db__,
                self.__nsubj__, self.__dobj__
            )
            resLA = find_relation(
                topBuff.type, topStack.type, self.__db__,
                self.__nsubj__, self.__dobj__
            )
            if resRA != "TBD":
                self.RA(resRA)
                if resRA == "nsubj":
                    self.__nsubj__ = True
                if resRA == "dobj":
                    self.__dobj__ = True
            elif resLA != "TBD":
                self.LA(resLA)
                if resLA == "nsubj":
                    self.__nsubj__ = True
                if resLA == "dobj":
                    self.__dobj__ = True
            # When both RA and LA doesn't happen
            # then shift the element on buffer to the top of the stack
            else:
                self.shift()
        # DONE !?
        return

    def AnalysisGrammarRelationTree(self, file: str):
        content = self.root.buildTree()
        __match = re.search("([\\/]([\\w\\s]+[\\.][a-z]+)$)", file)
        if __match is not None:
            _path = file[0: __match.start() + 1]
            Path(_path).mkdir(parents=True, exist_ok=True)
        with open(file, "w", encoding="utf-8") as fp:
            fp.seek(0)
            fp.write(content)
        return

    def print_buffer(self):
        __data = []
        __type = []
        for e in self.__buffer__:
            __data.append(e.data)
            __type.append(e.type)
        print(__data)
        print(__type)

    def print_stack(self):
        __data = []
        __type = []
        for e in self.__stack__:
            __data.append(e.data)
            __type.append(e.type)
        print(__data)
        print(__type)

    def debug(self):
        print("Buffer :")
        self.print_buffer()
        print("Stack  :")
        self.print_stack()

    def close(self):
        self.__db__.close()
