import string


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # mapping char(key) : char(lowercase)
        mapping = {}
        lowercase = string.ascii_lowercase
        pureKey = ""
        for char in key:
            if char != " " and char not in pureKey:
                pureKey += char
        for k, c in zip(pureKey, lowercase):
            mapping[k] = c

        decodeM = ""
        for m in message:
            if m in mapping:
                decodeM += mapping[m]
            else:
                decodeM += m
        return decodeM
