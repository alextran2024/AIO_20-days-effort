# bags of words
"""Lý thuyết: 
Bag of Words: hỗ trợ xử lý ngôn ngữ tự nhiên, mục đích phân loại text.
Phân tích và phân nhóm dựa theo “Bag of Words” (corpus). 
Với test data, tiến hành tìm ra số lần từng từ của test data xuất hiện trong “Bag”. 
Cách thức thực hiện:
– Bước 1: Chia nhỏ văn bản thành các từ riêng lẻ.
– Bước 2: Tạo một tập hợp các từ xuất hiện trong văn bản. Tập hợp này không
có phần tử trùng nhau.
– Bước 3: Biểu diễn văn bản input ở dạng vector: Mỗi câu (mỗi input) được
biểu diễn bằng một vector, với mỗi phần tử trong vector thể hiện số lần xuất
hiện của từ đó trong input.

Bài tập:
Tạo Bag-Of-Word cho tập dataset sau: corpus = ["Tôi thích môn Toán",
"Tôi thích AI", "Tôi thích âm nhạc"]. Sau đó tạo list có tên vector để lưu vector sau
khi thực hiện bước Tokenization đoạn văn bản sau: Tôi thích AI thích Toán, biết
Bag-Of-Word được sắp theo thứ tự tăng dần"""

# code:
corpus = ["Tôi thích môn Toán", "Tôi thích AI", "Tôi thích âm nhạc"]
BoW = sorted(set(word for sentence in corpus for word in sentence.split()))
print("BoW = ", BoW)

text = "Tôi thích AI thích Toán"
vector = [text.split().count(word) for word in BoW]
print("vector = ", vector)
