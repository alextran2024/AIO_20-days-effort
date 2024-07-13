# Max pooling và average

"""Tương tự như bài 6, tính tổng quát 1 matrix có thể tính max pooling và average, 
sau đó áp dụng test case cụ thể cho đề bài.
Không cho kernal size cụ thể, mặc định cho 2x2.

Các bước tiến hành:

1. Xác định matrix mới từ matrix ban đầu với bước nhảy stride 
    1.1. max_pol_mat có dimension new_rows = ((rows - pool_size)//stride +1) và new_cols = ((cols- pool_size)//stride +1))
    1.2. Gán max_pol_mat = 0 cho các phần tử, sau đó mới tính giá trị theo pooling hoặc average.
2. Tính max pooling:
    cho i chạy từ vị trí đầu (0) tới vị trí ((rows - pool_size)//stride +1), bước nhảy stride
        cho j chạy từ vị trí đầu (0) tới vị trí ((cols - pool_size)//stride +1), bước nhảy stride
        max_pol_mat = matrix[i][j] rồi cho duyệt qua pool_size
    ma trận result [i//stride][j//stride]
3. Tính average:
    cho i chạy từ vị trí đầu (0) tới vị trí (rows - pool_size +1), bước nhảy stride
        cho j chạy từ vị trí đầu (0) tới vị trí (cols - pool_size +1), bước nhảy stride
        tính tổng matrix mới rồi chia để lấy giá trị average
        sum_mat += matrix[i+m][j+n]
        avg_val = average[] khi cho duyệt qua pool_size
    ma trận result avg_mat [i//stride][j//stride]"""

# tính max_pooling:


def max_pooling(matrix, pool_size, stride):
    rows = len(matrix)
    cols = len(matrix[0])
    new_rows = ((rows - pool_size)//stride + 1)
    new_cols = ((cols - pool_size)//stride + 1)
    max_pol_mat = [[matrix[0]
                    for _ in range(new_rows)] for _ in range(new_cols)]

    for i in range(0, rows - pool_size + 1, stride):
        for j in range(0, cols - pool_size + 1, stride):
            max_pol = matrix[i][j]
            for m in range(pool_size):
                for n in range(pool_size):
                    max_pol = max(max_pol, matrix[i+m][j+n])
            max_pol_mat[i//stride][j//stride] = max_pol
    return max_pol_mat


# tính average:
def avg_pooling(matrix, pool_size, stride):
    rows = len(matrix)
    cols = len(matrix[0])
    new_rows = ((rows - pool_size)//stride + 1)
    new_cols = ((cols - pool_size)//stride + 1)
    avg_mat = [[matrix[0] for _ in range(new_rows)] for _ in range(new_cols)]

    for i in range(0, rows - pool_size + 1, stride):
        for j in range(0, cols - pool_size + 1, stride):
            sum_mat = 0
            for m in range(pool_size):
                for n in range(pool_size):
                    sum_mat += matrix[i+m][j+n]
            avg_val = sum_mat/(pool_size * pool_size)
            avg_mat[i//stride][j//stride] = avg_val
    return avg_mat


# Test case
A = [
    [0, 0, 0, 4],
    [0, 4, 0, 2],
    [0, 1, 0, 2],
    [0, 3, 0, 2]
]

pool_size = 2
stride = 2
result1 = max_pooling(A, pool_size, stride)
print("Ma trận max pooling từ A là ", result1)
result2 = avg_pooling(A, pool_size, stride)
print("Ma trận average từ A là ", result2)
