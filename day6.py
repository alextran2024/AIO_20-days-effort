# Ngày 6: Convolutional calculation bằng vòng lặp for
"""Padding với input là ma trận, kernel cho trước. Sau đó xử lý ra output. Không dùng numpy
Quy trình:
1. Xác định matrix A sau khi padding. 
    1.1.Tạo matrix pad_A với dimension là len(row A)+ biên và len (col A)+ biên. 
    (note: col A = len(A[0]))
    1.2.Cho các phần tử ban đầu của pad_A đều là 0, sau đó mới duyệt cho các phần tử của A vào pad. 
2. Tính convolutional matrix theo công thức tính ma trận.
3. Cho gía trị hàm A, B... cụ thể (test case)"""


def cal_pad_matrix(matrix, pad):
    rows = len(matrix)
    cols = len(matrix[0])
    new_rows = len(matrix) + pad*2
    new_cols = len(matrix[0]) + pad*2

    # 1.1
    pad_matrix = [[0 for _ in range(new_cols)] for _ in range(new_rows)]
    # 1.2
    for i in range(rows):
        for j in range(cols):
            pad_matrix[i+pad][j+pad] = matrix[i][j]
    return pad_matrix


def convolution(matrix, kernel, padding=0):
    """Thực hiện phép tính convolutional với padding."""
    # Thêm padding vào ma trận
    pad_matrix = cal_pad_matrix(matrix, padding)

    rows = len(pad_matrix)
    cols = len(pad_matrix[0])
    k_rows = len(kernel)
    k_cols = len(kernel[0])

    # Kích thước ma trận kết quả
    output_rows = rows - k_rows + 1
    output_cols = cols - k_cols + 1
    output_matrix = [[0 for _ in range(output_cols)]
                     for _ in range(output_rows)]

    # Thực hiện phép tích chập
    for i in range(output_rows):
        for j in range(output_cols):
            for ki in range(k_rows):
                for kj in range(k_cols):
                    output_matrix[i][j] += pad_matrix[i +
                                                      ki][j + kj] * kernel[ki][kj]

    return output_matrix


# Ma trận A và kernel B
A = [
    [0, 0, 0],
    [0, 4, 0],
    [0, 1, 0]
]

B = [
    [1, 1],
    [1, 1]
]

C = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]
# Tính convolutional A, B với zero padding và in kết quả
padding = 1
result1 = convolution(A, B, padding)

print("Output của A và kernel B với zero padding là: ", result1)

# Tính convolutional A, C:
padding = 1
result2 = convolution(A, C, padding)
print("Output của A và kernel C với zero padding là: ", result2)
