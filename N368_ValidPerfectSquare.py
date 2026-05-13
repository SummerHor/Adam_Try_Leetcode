class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if (num**0.5).is_integer():
            return True
        else:
            return False
