import numpy as np


def hourglass_np(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    lim_i = columns - 2
    lim_j = rows - 2

    sums = []
    lists = []

    for i in range(lim_i):
        for j in range(lim_j):
            hs = matrix[i:i + 3, j:j + 3]
            lists.append(hs)
            sum_ = np.sum(hs) - hs[1][0] - hs[1][2]
            sums.append(sum_)

    # print(sums)
    return max(sums)


def hourglass(arr):
    rows = len(arr)
    columns = len(arr[0])
    lim_i = columns - 2
    lim_j = rows - 2

    sums = []
    # lists = []
    for i in range(lim_i):
        for j in range(lim_j):
            hs = [arr[i][j:j + 3], [arr[i + 1][j + 1]], arr[i + 2][j:j + 3]]
            # lists.append(hourglass)
            sum_ = sum(sum(hs, []))
            sums.append(sum_)

    return max(sums)


# arr = []
#
# for _ in range(6):
#     arr.append(list(map(int, input().rstrip().split())))

arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]

# matrix = np.array(arr)
# print(hourglass_np(matrix))
print(hourglass(arr))
