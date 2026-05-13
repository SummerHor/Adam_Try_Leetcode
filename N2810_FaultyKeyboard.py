class Solution:
    def finalString(self, s: str) -> str:
        written_str = ""
        for char in s:
            if char != "i":
                written_str += char
            else:
                written_str = written_str[::-1]

        s = written_str
        return s
