class Solution:
    def toLowerCase(self, s: str) -> str:
        lowercase = ""
        for char in s:
            lowercase += char.lower()
        return lowercase
