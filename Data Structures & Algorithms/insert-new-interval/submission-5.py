class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda i:i[0])
        res=[intervals[0]]
        for index in range(1,len(intervals)):
            first = res[-1]
            if first[1] >= intervals[index][0]:
                res[-1] = [min(first[0],intervals[index][0]),max(first[1],intervals[index][1])]
            else:
                res.append(intervals[index])
        return res