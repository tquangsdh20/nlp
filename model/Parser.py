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

    def __init__(self, file_name: str = "./input/database.db"):
        # Make folder if not exists
        __match = re.search("([\\/]([\\w\\s]+[\\.][a-z]+)$)", file_name)
        if __match is not None:
            _path = file_name[0 : __match.start() + 1]
            Path(_path).mkdir(parents=True, exist_ok=True)
        # Connect the database
        self.conn = Connection(file_name)
        self.curr = self.conn.cursor()

    def init(self):
        """Init database with default requirements"""
        fp = open("./input/database.sql", encoding="utf-8")
        self.curr.executescript(fp.read())
        self.conn.commit()

    def close(self):
        self.conn.commit()
        self.curr.close()
        self.conn.close()


def isNumber(text: str):
    return text.isnumeric()


def isTime(text: str):
    return bool(re.search("(\\d+:\\d+)", text))

def isMaHieu(text: str):
    return bool(re.search("m\\d", text))

def lookup(word: str, db: Database):
    db.curr.execute(WORD_SEARCH.format(word=word))
    retVal = db.curr.fetchall()
    return retVal


def find_relation(
    first: str, second: str, db: Database, nsubj: bool = False, dobj: bool = False
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
        relation = (res[0])[0]
    return relation


def analysis(words: List[str], db: Database) -> List[Tuple[str, str]]:
    """Searching the list of words in database"""
    retLst: List[Tuple[str, str]] = []
    i: int = 0
    L: int = len(words)
    verb: bool = False
    while i < L:
        # Get the list of matching words
        lexicons = lookup(words[i].lower(), db)
        # Proceed item by item
        found: int = 0
        # Not found word in Dictionary
        if len(lexicons) == 0:
            # Check if it was type of NUMBER
            if isNumber(words[i]):
                retLst.append((f"{words[i]}", "NUM"))
            # Check if it was TIME-type
            elif isTime(words[i]):
                retLst.append((f"{words[i]}", "TIME"))
            elif isMaHieu(words[i]):
                retLst.append((f"{words[i]}", "NAME"))
            # In case of not matching any --> To be define
            else:
            # Due to simplization parser will skip unknown word
                # retLst.append((f"{words[i]}", "TBD"))
                pass
            i += 1
            continue
        # In case of found in Database
        Fwords = []
        while len(lexicons) > 0:
            # lexicon = word | number of words | type of word
            lexicon = lexicons.pop()
            word = lexicon[0]
            num = lexicon[1]
            wType = lexicon[2]
            jword: str = ""
            # Get the neibours of words with the number
            for j in range(num):
                jword += f" {words[i+j]}"
            if (jword.strip().lower() == word) and (found < num):
                # Check if get the other value will pop it
                if found > 0:
                    tmp = retLst.pop()
                    if tmp[1] == wType:
                        verb = False  # To reset found verb
                retLst.append((word, wType))
                found = num
                if wType == "VERB":
                    if ((word == "đến") or (word == "tới")) and verb:
                        # Skip đến/tới as "VERB"
                        retLst.pop()
                        found = 0  # Điều kiện để nhận từ mới phải reset lại
                    else:
                        verb = True  # To know that get verb already
            else:
                Fwords.append(jword.strip())
        if found == 0:
            raise Exception(
                f'NOT FOUND IN DATABASE: "{words[i]}" with the word list: {Fwords}'
            )
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

    def __init__(self, text: str, file: str = "./input/database.db"):
        __tmp = text.lower().replace("tp.", "tp ")
        __tmp = __tmp.replace(",", " ")
        self.root = Node(("ROOT", "ROOT"))
        self.__buffer__ = []
        self.__db__ = Database(file)
        self.__nSkip__ = 0
        self.__dobj__ = False  # To inform that if it found nsubj yet
        self.__nsubj__ = False  # To inform that if it found nsubj yet
        __words = analysis(__tmp.split(), self.__db__)
        for e in __words:
            self.__buffer__.append(Node(e))
        self.text = f"{self.getInfoWords()}"
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
        # - Is it VERB?
        if topBuffer.type == "VERB":
            # self.__verb__ = True
            # self.root.add_child(topBuffer, relation)
            pass
        else:  # Reduce
            # If have any relation with the remainding items
            dumpBffr = self.__buffer__.copy()
            while len(dumpBffr) > 0:
                item = dumpBffr.pop()
                if find_relation(topBuffer.type, item.type, self.__db__) != "TBD":
                    self.__nSkip__ += 1  # Counter reduce must be increased
                    return
            # No any relations with all the remainding items --> REDUCE
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
                topStack.type, topBuff.type, self.__db__, self.__nsubj__, self.__dobj__
            )
            resLA = find_relation(
                topBuff.type, topStack.type, self.__db__, self.__nsubj__, self.__dobj__
            )
            if resRA != "TBD":
                self.RA(resRA)
                # Inform that found nsubj & dobj yet.
                if resRA == "nsubj":
                    self.__nsubj__ = True
                if resRA == "dobj":
                    self.__dobj__ = True
            elif resLA != "TBD":
                self.LA(resLA)
                # Inform that found nsubj & dobj yet.
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
        content = f"{self.text}\n{self.root.buildTree()}"
        __match = re.search("([\\/]([\\w\\s]+[\\.][a-z]+)$)", file)
        if __match is not None:
            _path = file[0 : __match.start() + 1]
            Path(_path).mkdir(parents=True, exist_ok=True)
        with open(file, "w", encoding="utf-8") as fp:
            fp.seek(0)
            fp.write(content)
        return

    def getInfoWords(self):
        lex = []
        for e in self.__buffer__:
            lex.append((e.data, e.type))
        return lex

    def print_buffer(self):
        __data = []
        __type = []
        for e in self.__buffer__:
            __data.append(e.data)
            __type.append(e.type)
        __data.reverse()
        __type.reverse()
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
