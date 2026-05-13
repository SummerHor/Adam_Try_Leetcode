class Solution:
    def compress(self, chars: list[str]) -> int:
        if len(chars) < 2:
            return len(chars)
        compress = ""
        count = 1
        i1, i2 = 0, 1

        while i2 < len(chars):
            if chars[i1] == chars[i2]:
                count += 1
            else:
                if count == 1:
                    compress += chars[i1]
                else:
                    compress = compress + chars[i1] + str(count)
                    count = 1
            i1 += 1
            i2 += 1
        compress = compress + chars[i1] + str(count)
        print(compress)
        return len(compress)


print(
    Solution().compress(
        ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    )
)
