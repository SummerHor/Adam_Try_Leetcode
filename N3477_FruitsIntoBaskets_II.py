class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for f in fruits:
            for i, b in enumerate(baskets):
                if f <= b:
                    baskets.pop(i)
                    break
        return len(baskets)
