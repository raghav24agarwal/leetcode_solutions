class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
        n = len(nums)
        
        start = 0
        end = 0

        win_size = 0
        count = 0

        while end<n:
            if nums[end]>=left and nums[end]<=right:
                win_size = end-start+1
                count+=win_size
            elif nums[end]<left:
                count+=win_size
            elif nums[end]>right:
                win_size = 0
                start = end+1
                
            end+=1

        return count