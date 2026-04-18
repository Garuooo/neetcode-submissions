class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        intervals.sort(key = lambda i: i[0])
        res=[intervals[0]]
        for i in range(1,len(intervals)):
            first=res[-1]
            if first[1] >= intervals[i][0]:
                new_interval=[first[0],max(first[1],intervals[i][1])]
                res[-1] = new_interval
            else:
                res.append(intervals[i])

        return res