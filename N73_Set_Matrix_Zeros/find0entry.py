def find0entry(matrix: list[list[int]]) -> set[tuple[int, int]]:
    entry0 = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                entry0.add((i, j))
    return entry0


# print(find0entry([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
