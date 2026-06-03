class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        mapping = {}
        for num in nums:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1

        for num in mapping:
            if mapping[num] % 2 != 0:
                return False
        return True


print(Solution().divideArray([3, 2, 3, 2, 2, 2]))
