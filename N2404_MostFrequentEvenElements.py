from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]):

        # mapping even : fre
        mapping = {}
        # sort arr
        nums.sort()

        for num in nums:
            if num % 2 == 0:
                if num not in mapping:
                    mapping[num] = 1
                else:
                    mapping[num] += 1

        if not mapping:
            return -1
        # sort mapping by occurrence
        mapping = dict(sorted(mapping.items(), key=lambda item: item[1]))
        # return mapping
        MF = list(mapping.values())[-1]  # max fre

        for even in mapping:
            if mapping[even] == MF:
                return even
        return -1


print(Solution().mostFrequentEven(nums=[0, 1, 4, 2, 2, 4, 1]))
print(Solution().mostFrequentEven(nums=[4, 4, 4, 9, 2, 4]))

print(Solution().mostFrequentEven(nums=[29, 47, 21, 41, 13, 37, 25, 7]))
