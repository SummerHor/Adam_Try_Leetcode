class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        mapping = {}
        result = []
        for num in nums:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1
            if mapping[num] == 2:
                result.append(num)
        for num in range(1, max(nums) + 2):
            if num not in nums:
                result.append(num)
                return result
