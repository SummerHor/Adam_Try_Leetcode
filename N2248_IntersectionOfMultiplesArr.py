class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        mapping = {}
        arr = []
        for num in nums:
            arr += num
        arr.sort()
        intersect_arr = []
        for num in arr:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1

        for num in mapping:
            if mapping[num] == len(nums):
                intersect_arr.append(num)
        return intersect_arr
