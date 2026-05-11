class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        transpose_matrix = []
        for i, row in enumerate(matrix):
            if i == 0:
                for entry in row:
                    transpose_matrix.append([entry])
            else:
                for entry, t_row in zip(row, transpose_matrix):
                    t_row.append(entry)
        return transpose_matrix
