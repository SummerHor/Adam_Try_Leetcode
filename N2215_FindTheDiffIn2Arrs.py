class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        l1 = []
        l2 = []
        for num in set1:
            if num not in set2:
                l1.append(num)
        for num in set2:
            if num not in set1:
                l2.append(num)
        return [l1, l2]
