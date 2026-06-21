from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        # Find Min Rows
        minRows = [min(row) for row in matrix]
        minRows = set(minRows)

        # 2. find max Columns
        # step 1: initialize the maximums with the first row
        max_cols = list(matrix[0])

        # step 2: loop through the remaining rows (from index 1 to the end)
        for row in matrix[1:]:
            # loop through each column index
            for i in range(len(row)):
                # if the current element is greater than our stored max, update it
                if row[i] > max_cols[i]:
                    max_cols[i] = row[i]
        lucky = []
        for num in max_cols:
            if num in minRows:
                lucky.append(num)
        return lucky
