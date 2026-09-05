"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # if only one meeting -> true
        n = len(intervals)
        if n <= 1:
            return True
        
        # sort by start time
        intervals.sort(key=lambda interval: interval.start)

        # iterate current start time less than prev end time or not
        for i in range(1, n):
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True

