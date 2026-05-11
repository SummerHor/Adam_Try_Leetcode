class Solution:
    def duplicateNumbersXOR(self, nums: list[int]) -> int:
        mapping = {}
        dupNum = 0
        for num in nums:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1
        for num in mapping:
            if mapping[num] == 2:
                dupNum ^= num
        return dupNum
