class Solution:
    def compress(self, chars: list[str]) -> int:
        if len(chars) < 2:
            return len(chars)

        write = 0
        count = 1
        i1, i2 = 0, 1

        while i2 <= len(chars):  # Use <= to handle the last group logic
            # Check if we are still seeing the same character
            if i2 < len(chars) and chars[i1] == chars[i2]:
                count += 1
            else:
                # write to the array
                chars[write] = chars[i1]
                write += 1

                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1

                # Reset for the next character group
                count = 1
                i1 = i2

            i2 += 1

        return write
