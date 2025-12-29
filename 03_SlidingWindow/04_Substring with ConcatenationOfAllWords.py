# 30. Substring with Concatenation of All Words

# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings.
# "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.

# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

class Solution:
    def checkSubstring(self, mp, subStr, wordLen):
        for j in range(0, len(subStr), wordLen):
            w = subStr[j: j+wordLen]
            if w in mp:
                mp[w] -= 1
                if mp[w] == -1:
                    return False
            else:
                return False
        return True
    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        wordLen = len(words[0])
        sLen = len(s)
        wordsWindow = len(words) * wordLen
        mp = dict()
        for x in words:
            if x in mp:
                mp[x] += 1
            else:
                mp[x] = 1
        i = 0
        while(i + wordsWindow <= sLen):
            if(self.checkSubstring(mp.copy(), s[i:i+wordsWindow], wordLen)):
                res.append(i)
            i += 1
        return res
        
