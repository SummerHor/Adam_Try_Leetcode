class Solution:
    def twoOutOfThree(
        self, nums1: list[int], nums2: list[int], nums3: list[int]
    ) -> list[int]:
        result = []
        for num in set(nums1):
            if num in nums2 or num in nums3:
                result.append(num)
        for num in nums2:
            if num not in result and num in nums3:
                result.append(num)
        return result
