class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # sum2, sum1 are sum of bobSizes and aliceSizes, respectively
        sum2 = sum(bobSizes)
        sum1 = sum(aliceSizes)
        # This is the 'target' difference Alice's bar needs to bridge
        diff = (sum2 - sum1) / 2
        set2 = set(bobSizes)
        for c in aliceSizes:
            if c + diff in set2:
                return [c, c + diff]
