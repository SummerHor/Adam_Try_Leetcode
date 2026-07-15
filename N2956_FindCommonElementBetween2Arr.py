from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Initialize 2 dictionaries, where dict_i = {num : fre}
        mapping1 = {}
        mapping2 = {}
        ans1, ans2 = 0, 0
        for n in nums1:
            if n not in mapping1:
                mapping1[n] = 1
            else:
                mapping1[n] += 1

        for num in nums2:
            if num not in mapping2:
                mapping2[num] = 1
            else:
                mapping2[num] += 1

        for num in mapping1:
            if num in mapping2:
                ans1 += mapping1[num]

        for num in mapping2:
            if num in mapping1:
                ans2 += mapping2[num]

        return [ans1, ans2]
