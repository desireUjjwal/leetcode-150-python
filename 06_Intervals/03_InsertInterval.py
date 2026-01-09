# 57. Insert Interval

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and
# intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res

  # Another approach but tricky better to go with above approach if found something similar to this
  class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        i = 0
        while(i < n and intervals[i][1] < newInterval[0]):
            res.append(intervals[i])
            i += 1
        while(i < n and intervals[i][0] <= newInterval[1]):  # very tricky condition to merge 
            min_el = min(newInterval[0], intervals[i][0])
            max_el = max(newInterval[1], intervals[i][1])
            newInterval = [min_el, max_el]
            i += 1
        
        res.append(newInterval)
        res += intervals[i : ]
        return res
