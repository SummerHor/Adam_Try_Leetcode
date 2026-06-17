class Solution:
    # Run-Length Encoding
    def RLE(self, string: str):
        if not string:
            return "Empty String"

        count = 1
        temp = string[0]
        rle = ""
        for char in string[1:]:
            if char == temp:
                count += 1
            else:
                rle = rle + str(count) + temp
                # reset the char and the frequency of consecutive chars
                temp = char
                count = 1
        # concentinate for the last characters
        rle = rle + str(count) + temp
        return rle

    def countAndSay(self, n: int) -> str:
        if n > 1:
            string = "1"
        else:
            return str(n)
        for i in range(n - 1):
            rle = self.RLE(string)
            string = rle
        return rle
