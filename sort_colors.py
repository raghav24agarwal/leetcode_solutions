class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        start = 0
        index = 0
        end = n-1
        
        while(index<=end):
            if nums[index] == 0:
                nums[index], nums[start] = nums[start], nums[index]
                index+=1
                start+=1
            elif nums[index] == 1:
                index+=1
            elif nums[index] == 2:
                nums[index], nums[end] = nums[end], nums[index]
                end-=1