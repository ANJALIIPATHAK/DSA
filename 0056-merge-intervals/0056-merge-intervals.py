class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []

        for i in range(0,len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if(res and end <= res[-1][1]):
                continue
            for j in range(i+1, len(intervals)):
                if(intervals[j][0] <= end):
                    end = max(end, intervals[j][1])
                else:
                    break
            res.append([start, end])
        return res

