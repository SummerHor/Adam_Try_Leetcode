# I just used the simple linear search for now
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        for num in nums:
            if num == target:
                return True
        return False
