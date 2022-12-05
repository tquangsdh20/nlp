# BÀI TẬP LỚN MÔN XỬ LÝ NGÔN NGỮ TỰ NHIÊN
#### Tran Quang - 2070426

## Đề Bài
Xây dựng hệ thống hỏi đáp đơn giản về các chuyến bay nội địa bằng **quan hệ văn phạm**.

## Cơ sở dữ liệu các chuyến bay

Dữ liệu về các chuyến bay có sẵn trong hệ thống gồm 3 bảng sau:

<p align="center">
    <div align="center">
        <table border="1" class="dataframe">
            <thead>
				<h4>MÁY BAY</h4>
                <tr style="text-align: right;"><th>flight</th></tr>
            </thead>
            <tbody>
                <tr><th>M1</th></tr>
                <tr><th>M2</th></tr>
                <tr><th>M3</th></tr>
                <tr><th>M4</th></tr>
                <tr><th>M5</th></tr>
                <tr><th>M6</th></tr>
            </tbody>
        </table>
    </div>
</p>

<p align="center">
    <div align="center">
        <table border="1" class="dataframe">
            <thead>
				<h4>CHUYẾN BAY ĐI - ATIME</h4>
                <tr style="text-align: right;"><th>id</th><th>flight</th><th>place</th><th>time</th></tr>
            </thead>
            <tbody>
                <tr><th>1</th><td>M1</td><td>HUE</td>     <td>11:00HR</td></tr>
                <tr><th>2</th><td>M2</td><td>HUE</td>     <td>13:30HR</td></tr>
                <tr><th>3</th><td>M3</td><td>HCM</td>     <td>16:30HR</td></tr>
                <tr><th>4</th><td>M4</td><td>HAIPHONG</td><td>10:30HR</td></tr>
                <tr><th>5</th><td>M5</td><td>HN</td>      <td>05:45HR</td></tr>
                <tr><th>6</th><td>M6</td><td>HAIPHONG</td><td>11:30HR</td></tr>
            </tbody>
        </table>
    </div>
</p>

<p align="center">
    <div align="center">
        <table border="1" class="dataframe">
            <thead>
				<h4>CHUYẾN BAY ĐẾN - DTIME</h4>
                <tr style="text-align: right;"><th>id</th><th>flight</th><th>place</th><th>time</th></tr>
            </thead>
            <tbody>
                <tr><th>1</th><td>M1</td><td>HCMC</td><td>10:00HR</td></tr>
                <tr><th>2</th><td>M2</td><td>HN</td><td>12:30HR</td></tr>
                <tr><th>3</th><td>M3</td><td>DANANG</td><td>15:00HR</td></tr>
                <tr><th>4</th><td>M4</td><td>DANANG</td><td>08:30HR</td></tr>
                <tr><th>5</th><td>M5</td><td>HCM</td><td>03:30HR</td></tr>
                <tr><th>6</th><td>M6</td><td>HCMC</td><td>09:30HR</td></tr>
            </tbody>
        </table>
    </div>
</p>

<p align="center">
    <div align="center">
        <table border="1" class="dataframe">
            <thead>
				<h4>RUN-TIME</h4>
                <tr style="text-align: right;"><th>id</th><th>flight</th><th>src</th><th>dest</th><th>time</th></tr>
            </thead>
            <tbody>
                <tr><th>1</th><td>M1</td><td>HCMC</td><td>HUE</td><td>1:00HR</td></tr>
                <tr><th>2</th><td>M2</td><td>HN</td><td>HUE</td><td>1:00HR</td></tr>
                <tr><th>3</th><td>M3</td><td>DANANG</td><td>HCM</td><td>1:30HR</td></tr>
                <tr><th>4</th><td>M4</td><td>DANANG</td><td>HAIPHONG</td><td>02:00HR</td></tr>
                <tr><th>5</th><td>M5</td><td>HCM</td><td>HN</td><td>02:15HR</td></tr>
                <tr><th>6</th><td>M6</td><td>HCMC</td><td>HAIPHONG</td><td>02:00HR</td></tr>
            </tbody>
        </table>
    </div>
</p>

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

Để thực hiện được code sau cần cài đặt Python 3.7.15 và cài đặt môi trường theo file *enviroment.yml*. Source code gồm có 3 folders:

1.	input: những file input vào gồm những câu cần phân tích ngữ pháp
2.	output: những file xuất ra kết quả phân tích cho các câu hỏi 
3.	models: những file source code được viết bằng Python

# Build and Test
TODO: Describe and show how to build your code and run the tests. 

Author: Tran Quang - 2070426
