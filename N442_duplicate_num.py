class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        # use to store the first occurrence number
        map = set()
        duplicate_nums = []
        for num in nums:
            if num not in map:
                map.add(num)
            else:
                duplicate_nums.append(num)
        return duplicate_nums
