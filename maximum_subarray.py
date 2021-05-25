class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_so_far = -999999
        max_ending_here = 0
        n = len(nums)
        
        for i in range(n):
            max_ending_here += nums[i]
            if max_ending_here<nums[i]:
                max_ending_here = nums[i]
                
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
                
                
        return max_so_far