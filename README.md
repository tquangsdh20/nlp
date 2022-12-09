# BÀI TẬP LỚN MÔN XỬ LÝ NGÔN NGỮ TỰ NHIÊN

#### Tran Quang - 2070426

## Đề Bài
Xây dựng hệ thống hỏi đáp đơn giản về các chuyến bay nội địa bằng **quan hệ văn phạm**.

## Cơ sở dữ liệu các chuyến bay

Dữ liệu về các chuyến bay có sẵn trong hệ thống gồm 4 bảng sau:

<p align="center"><img src="https://user-images.githubusercontent.com/87520683/206459244-3a44ab03-cead-485b-b46b-2680d62cf563.png"> <img src="https://user-images.githubusercontent.com/87520683/206459281-16fbc036-7eec-4263-9cde-498a6bdfbb7e.png"> </p>
<p align="center"><img src="https://user-images.githubusercontent.com/87520683/206459301-4a9434c5-6bf5-4dae-97f7-6eca2f116cb9.png"> <img src="https://user-images.githubusercontent.com/87520683/206459323-c163b1b5-dd44-4931-9823-60c0cb94f865.png"></p>

## Các câu truy vấn

Cho các câu truy vấn như sau:

- Máy bay nào đến thành phố Huế lúc 13:30HR ?.
- Máy bay nào bay từ Đà Nẵng đến TP. Hồ Chí Minh mất 1 giờ ?.
- Hãy cho biết mã hiệu các máy bay bay đến Huế ?.
- Máy bay nào xuất phát từ Tp.Hồ Chí Minh, lúc mấy giờ ?.
- Máy bay nào bay từ TP.Hồ Chí Minh đến Hà Nội ?.
- Máy bay M5 có xuất phát từ Đà Nẵng không ?.
- Thời gian máy bay M6 bay từ TP.HCM đến Hải Phòng mất mấy giờ ?.
- Có máy bay nào xuất phát từ Hải phòng không ?.

## TODO: 

Viết chương trình thực hiện:

1. Xây dựng bộ phân tích cú pháp của văn phạm phụ thuộc.
2. Phân tích cú pháp và xuất ra các quan hệ của các thành phần của từng câu truy vấn.
3. Từ kết quả ở trên, tạo các quan hệ văn phạm cho các chuyến máy bay giữa thành phố Hồ Chí Minh, Huế, Đà Nẵng Hải Phòng và Hà Nội với cơ sở dữ liệu đã cho ở trên.
4. Tạo dạng luận lý từ các quan hệ văn phạm ở câu 3.
5. Tạo ngữ nghĩa thủ tục từ dạng luận lý ở câu trên.
6. Truy xuất dữ liệu để tìm thông tin trả lời cho các câu truy vấn trên.

## Nội dung thực thi

### Ngôn ngữ sử dụng: Python

Để thực hiện được code sau cần cài đặt Python 3.7.15

Project gồm có 3 folders chính:

1.	input: những file input vào gồm những câu cần phân tích ngữ pháp và cơ sở dữ liệu
2.	output: những file xuất ra kết quả phân tích cho các câu hỏi 
3.	model: những file source code được viết bằng Python

## Thực hiện chương trình

TODO: Đoạn lệnh thực thi được viết ở file `main.py` như sau:

``` py
from model.Parser import Parser, Database

if __name__ == "__main__":
    # Cau 1: Xây dựng bộ phân tích cú pháp
    db = Database()
    db.init()
    db.close()
    fp = open("./input/query.csv", "r", encoding="utf-8")
    lines = fp.readlines()
    # Cau 2: Phân tích cú pháp và xuất ra các quan hệ của các thành phần của từng câu truy vấn.
    for index in range(len(lines)):
        parser = Parser(lines[index])
        parser.do_MaltParser()
        parser.AnalysisGrammarRelationTree(f"./output/output{index+1}.txt")
```

Kết quả xuất ra được lưu ở folder: `./output/`

