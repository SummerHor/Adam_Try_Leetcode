class Solution:
    def count_digit(self, num):
        count_digit = 0
        while num > 0:
            num //= 10
            count_digit += 1
        return count_digit

    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if self.count_digit(num) % 2 == 0:
                count += 1
        return count
