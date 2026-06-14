class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        mapping = {}
        for num in nums:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1
        max_fre = max(list(mapping.values()))

        hig_degree = []
        for n in mapping:
            if mapping[n] == max_fre:
                hig_degree.append(n)

        min_len = []

        # RESET POINTERS INSIDE THE LOOP HERE
        for high in hig_degree:
            left = 0
            right = len(nums) - 1

            # Move left pointer rightward
            while left <= right and nums[left] != high:
                left += 1

            # Move right pointer leftward
            while right >= left and nums[right] != high:
                right -= 1

            min_len.append(right - left + 1)

        return min(min_len)
