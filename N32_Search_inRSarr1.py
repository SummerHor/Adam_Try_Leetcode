# simple linear search only
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        count_index = 0
        for num in nums:
            if num == target:
                return count_index
            count_index += 1
        return -1
