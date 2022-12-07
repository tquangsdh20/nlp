from model import Parser, Database


if __name__ == "__main__":
    # Initialization
    db = Database("./input/database.db")
    # fp = open("./input/query.csv")
    with open("./input/query.csv",'r', encoding="utf-8") as fp:
        lines = fp.readlines()
        for line in lines:
            p = Parser(line, db)
            p.do_MaltParser()
            p.AnalysisGrammarRelationTree(f"./output/output{lines.index(line)}.txt")

    p = Parser("Máy bay nào bay từ Đà Nẵng đến TP. Hồ Chí Minh mất 1 giờ ?.")