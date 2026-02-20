# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def helper(i, ds, ans):
            if(i == len(digits)):
                ans.append(ds)
                return
            string = phone_map[digits[i]]
            for j in range(len(string)):
                ds += string[j]
                helper(i+1, ds, ans)
                ds = ds[:-1]
        ans = []
        ds = ''
        helper(0, ds, ans)
        return ans
