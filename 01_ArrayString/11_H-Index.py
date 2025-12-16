# 274. H-Index
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: 
# The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        step = 0
        n = len(citations)
        for x in citations[::-1]:
            step += 1
            if x >= step:
                continue
            else:
                return step-1
        return step
