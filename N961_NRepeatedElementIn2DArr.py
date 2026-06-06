class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        store = set()
        for num in nums:
            if num not in store:
                store.add(num)
            else:
                return num
