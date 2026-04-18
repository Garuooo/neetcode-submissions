class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: (i[0],i[1]))

        prevEnd=intervals[0][1]
        count=0
        for start,end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                count+=1
                prevEnd=min(end,prevEnd)

        return count