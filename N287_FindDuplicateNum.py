class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mapping = {}
        for num in nums:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1
        for num in mapping:
            if mapping[num] > 1:
                return num
