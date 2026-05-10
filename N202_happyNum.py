class Solution:
    def isHappy(self, n: int) -> bool:
        store_visited_num = set()
        store_visited_num.add(n)
        while True:
            if n == 1:
                return True
            n = self.sum_pow2(n)
            if n in store_visited_num:
                return False
            store_visited_num.add(n)

    def sum_pow2(self, integer):
        results = 0
        while integer > 0:
            results = results + pow((integer % 10), 2)
            integer //= 10
        return results
