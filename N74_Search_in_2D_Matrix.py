class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            for entry in row:
                if target == entry:
                    return True
        return False
