# 68. Text Justification

# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
# Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. 
# If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        currLine, width = [], 0
        i = 0
        while i < len(words):
            if width + len(words[i]) <= maxWidth:
                currLine.append(words[i])
                width += len(words[i]) + 1
                i += 1
            else:
                totalSpaces = maxWidth - width + len(currLine)
                spacesAdded = 0
                j = 0
                while spacesAdded < totalSpaces:
                    if j >= len(currLine) - 1:
                        j = 0
                    currLine[j] += " "
                    j += 1
                    spacesAdded += 1
                result.append("".join(currLine))
                currLine = []
                width = 0
        for i in range(0, len(currLine) - 1):
            currLine[i] += " "
        remainingSpace = maxWidth - width + 1 # last space is extra added in width that's why +1
        currLine[-1] += " " * remainingSpace
        result.append("".join(currLine))
        return result
