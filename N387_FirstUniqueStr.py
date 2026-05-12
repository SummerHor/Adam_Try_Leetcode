class Solution:
    def firstUniqChar(self, s: str) -> int:
        store_index = {}
        index = 0
        for char in s:
            if char not in store_index:
                store_index[char] = [1, index]
            else:
                store_index[char][0] += 1

            index += 1
        for char in store_index:
            if store_index[char][0] == 1:
                return store_index[char][1]
        return -1


print(Solution().firstUniqChar("loveleetcode"))
