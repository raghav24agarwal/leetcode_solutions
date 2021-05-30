class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        n = len(intervals)
        result = []
        result.append(intervals[0])
        
        i = 1
        while i<=n-1:
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
                
            else:
                result.append(intervals[i])
                
            i+=1

        return result