# 383. Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countChar = {}
        for c in magazine:
            countChar[c] = 1 + countChar.get(c, 0)
        
        for c in ransomNote:
            if c in countChar:
                countChar[c] -= 1
                if countChar[c] == -1:
                    return False
            else:
                return False
        return True
