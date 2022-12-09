from model.Parser import Parser, Database


if __name__ == "__main__":
    # Cau 1: Xây dựng bộ phân tích cú pháp --> model/Parser.py
    db = Database()
    db.init()
    db.close()
    fp = open("./input/query.csv", "r", encoding="utf-8")
    lines = fp.readlines()
    # Cau 2: Phân tích cú pháp và xuất ra các quan hệ của các thành phần của từng câu truy vấn.
    for index in range(len(lines)):
        parser = Parser(lines[index])
        # print(parser.text)
        parser.do_MaltParser()
        parser.AnalysisGrammarRelationTree(f"./output/output{index+1}.txt")
