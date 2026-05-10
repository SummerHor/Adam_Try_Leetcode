class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        index_list_toInsert = []
        for i in range(len(arr)):
            if arr[i] == 0:
                index_list_toInsert.append(i + len(index_list_toInsert))
        if index_list_toInsert:
            for index in index_list_toInsert:
                if index <= len(arr):
                    arr.insert(index, 0)
            for i in range(len(index_list_toInsert)):
                arr.pop(-1)
        return arr
