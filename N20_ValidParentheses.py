class Solution:
    def isValid(self, s: str) -> bool:
        # using stalk to do the validation
        stack = []  # LIFO
        validP = {"}": "{", ")": "(", "]": "["}

        if len(s) < 2:
            return False

        for p in s:
            # stack the open parentheses
            if p not in validP:
                stack.append(p)
            else:  # if the parentheses is inside the validP which is the close parentheses,
                # then check if it is the last element in the stack. If it is, then pop that item and continue iterating process.
                # otherwise return that it is invalid parentheses.
                if stack and validP[p] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
        return not stack
