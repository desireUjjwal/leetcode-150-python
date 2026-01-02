# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if (x == "(" or x == "{" or x == "["):
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top == "(" and x != ")":
                    return False
                elif top == "{" and x != "}":
                    return False
                elif top == "[" and x != "]":
                    return False
        return True if len(stack) == 0 else False
