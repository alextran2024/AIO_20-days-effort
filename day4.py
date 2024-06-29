# tính ma trận tích chập
"""phân tích bài toán:
1. Khai báo các ma trận a, k ban đầu
2. Tính tích chập:
* Tính gía trị của ma trận tích chập tại từng vị trí: 
Duyệt qua hàng i của a và từng cột n của k: = sum(vị trí[i] của a + vị trí [n] của k) với n = range (0, k+1)"""

# Định nghĩa ma trận A và kernel B
mat_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

kernal = [
    [2, 4],
    [1, 3]
]

# Khởi tạo ma trận kết quả
result = [[0 for _ in range(len(mat_a[0]) - len(kernal[0]) + 1)]
          for _ in range(len(mat_a) - len(kernal) + 1)]

# Tính toán tích chập
for i in range(len(result)):
    for j in range(len(result[0])):
        sum_val = 0
        for ki in range(len(kernal)):
            for kj in range(len(kernal[0])):
                sum_val += mat_a[i + ki][j + kj] * kernal[ki][kj]
        result[i][j] = sum_val

# In ma trận kết quả
print(result)

# bài 2
kernal_C = [
    [1, 1, 1],
    [0, 0, 0],
    [1, 1, 1]
]
result2 = [[0 for _ in range(len(mat_a[0]) - len(kernal_C[0]) + 1)]
           for _ in range(len(mat_a) - len(kernal_C) + 1)]

for i in range(len(result2)):
    for j in range(len(result2[0])):
        sum_val2 = 0
        for ki in range(len(kernal_C)):
            for kj in range(len(kernal_C[0])):
                sum_val2 += mat_a[i + ki][j + kj] * kernal_C[ki][kj]
        result2[i][j] = sum_val2

# In ma trận kết quả
print(result2)
