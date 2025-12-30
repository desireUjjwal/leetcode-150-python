# 30. Substring with Concatenation of All Words

# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings.
# "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.

# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

class Solution:
    def checkSubstring(self, wordCount, subStr, wordLen):
        for s in range(0, len(subStr), wordLen):
            word = subStr[s: s+wordLen]
            if word in wordCount:
                wordCount[word] -= 1
                if(wordCount[word] == -1):
                    return False
            else:
                return False
        return True


    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        wordLen = len(words[0])
        windowSize = len(words) * wordLen
        wordsCount = {}
        for w in words:
            wordsCount[w] = 1 + wordsCount.get(w, 0)

        i = 0
        while(i + windowSize <= len(s)):
            if(self.checkSubstring(wordsCount.copy(), s[i: i + windowSize], wordLen) == True):
                res.append(i)
            i += 1
        return res
    
