class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True

        # Keep track of the exact original mismatch order: (c1, c2)
        first_mismatch = None
        count = 0

        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                count += 1
                if count > 2:
                    return False

                if first_mismatch is None:
                    # Save the exact order seen at the first mismatch
                    first_mismatch = (c1, c2)
                else:
                    # For the second mismatch, it MUST be perfectly mirrored (c2, c1)
                    if (c2, c1) != first_mismatch:
                        return False

        return count == 2


print(Solution().areAlmostEqual("bank", "kanb"))
