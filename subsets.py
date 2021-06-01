class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        
        def backtracking(index, n, subset, result):
            result.append(list(subset))
        
            for i in range(index, n):
                subset.append(nums[i])
                backtracking(i+1, n, subset, result)
                subset.pop()
                
        result = []
        backtracking(0, n, [], result)
        
        return result