class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mapping = {}
        lucky_list = []
        for num in arr:
            if num not in mapping:
                mapping[num] = 1
            else:
                mapping[num] += 1
        for num in mapping:
            if mapping[num] == num:
                lucky_list.append(num)
        if lucky_list:
            return max(lucky_list)
        return -1
