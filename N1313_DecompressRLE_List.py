class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed_list = []
        if len(nums) < 2:
            return nums
        for i, j in zip(range(0, len(nums) + 1, 2), range(1, len(nums) + 1, 2)):
            decompressed_list += [nums[j]] * nums[i]
        return decompressed_list
