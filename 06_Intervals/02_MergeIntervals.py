# 56. Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            curr_f = intervals[i][0]
            curr_b = intervals[i][1]
            prev_b = res[-1][1]

            if prev_b >= curr_f and prev_b < curr_b:
                res[-1][1] = curr_b
            elif curr_f > prev_b:
                res.append(intervals[i])
        return res
