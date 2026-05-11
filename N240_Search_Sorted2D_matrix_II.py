# I only search for the rows whose last entry is greater than target number, and I search backward inisde those rows.
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] >= target:
                for entry in row[::-1]:
                    if target == entry:
                        return True
        return False
