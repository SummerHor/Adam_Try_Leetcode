import find0entry as f0


# print(f0.find0entry(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
#
def setZeros(matrix):
    # Entries 0
    entries = f0.find0entry(matrix)
    for entry in entries:
        row_i, col_j = entry
        for col in range(len(matrix[row_i])):
            matrix[row_i][col] = 0
        for row in range(len(matrix)):
            matrix[row][col_j] = 0
    return matrix


print(setZeros(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
print(setZeros([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
