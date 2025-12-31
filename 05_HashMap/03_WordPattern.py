# 290. Word Pattern

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        charToWord, wordToChar = {}, {}

        for i in range(len(pattern)):
            c , word = pattern[i], words[i]
            if ((c in charToWord and charToWord[c] != word) or
                (word in wordToChar and wordToChar[word] != c)):
                return False
            charToWord[c] = word
            wordToChar[word] = c
        return True

  # Using zip function
  class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        charToWord, wordToChar = {}, {}

        for c, word in zip(pattern, words):
            if ((c in charToWord and charToWord[c] != word) or
                (word in wordToChar and wordToChar[word] != c)):
                return False
            charToWord[c] = word
            wordToChar[word] = c
        return True
