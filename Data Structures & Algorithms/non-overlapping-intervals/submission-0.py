class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:i[0])
        print(intervals)
        count=0
        for i in range(1,len(intervals)):
            first=intervals[i-1]
            second=intervals[i]

            if first[1] > second[0]:
                if second[1] > first[1]:
                    second[1]=first[1]
                count+=1
        return count