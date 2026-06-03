class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        set2 = set(arr2)
        surfixArr = []
        mapping = {}
        for i in arr1:
            if i in set2:
                if i not in mapping:
                    mapping[i] = 1
                else:
                    mapping[i] += 1
            else:
                surfixArr.append(i)
        surfixArr.sort()
        result = []
        for i in arr2:
            if i in mapping:
                result += [i] * mapping[i]
        return result + surfixArr
