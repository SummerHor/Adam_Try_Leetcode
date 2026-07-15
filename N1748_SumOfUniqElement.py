from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        # Hash map used to store uinque element
        mapping = {}
        for num in nums:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1

        Sum = 0
        for num in mapping:
            if mapping[num] == 1:
                Sum += num
        return Sum
