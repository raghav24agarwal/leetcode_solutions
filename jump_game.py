class Solution:
    
    def canJump(self, nums: List[int]) -> bool:
        
        jump = 0
        n = len(nums)
        
        for i in range(0,n):
            
            if jump<i:
                return False
            
            jump = max(jump,i+nums[i])
            if jump>=n:
                return True
            
        return True