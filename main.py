import sqlite3 as sql
from model.Parser import Parser, Database

def init():
    with sql.Connection("./input/database.db") as db:
        curr = db.cursor()
        fp = open("./input/database.sql", encoding = "utf-8")
        curr.executescript(fp.read())
        fp.close()
        db.commit()
        curr.close()
    pass

if __name__ == "__main__":
    # Initialization
    db = Database("./input/database.db")
    # fp = open("./input/query.csv")
    with open("./input/query.csv",'r', encoding="utf-8") as fp:
        lines = fp.readlines()
        for line in lines:
            print(line.strip())
            p = Parser(line, db)
            p.do_MaltParser()
            p.AnalysisGrammarRelationTree(f"./output/output{lines.index(line)}.txt")
