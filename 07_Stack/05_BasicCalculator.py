# 224. Basic Calculator

# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        res = 0
        sign = 1
        stack = []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "-+":
                res += num * sign
                sign = 1 if c == '+' else -1
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += num * sign
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num * sign
