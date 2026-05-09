class Solution:
    def singleNumber(self, nums: list[int]):
        mapping = {}  # storing #of num : occurrance
        for num in nums:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1
        for num in mapping.keys():
            if mapping[num] == 1:
                return num
