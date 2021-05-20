class Solution(object):
    def threeSumClosest(self, nums, target):
        
        length = len(nums)
        
        fixed = 0
        
        minn = 99999
        
        nums.sort()
        
        while(fixed<length-2):
            
            left = fixed+1
            right = length-1
            
            while(left<right):
                
                summ = nums[fixed] + nums[left] + nums[right]
                
                if abs(target-summ)<minn:
                    minn = abs(target-summ)
                    result = summ
                    
                if summ<=target:
                    left+=1
                else:
                    right-=1
                    
            fixed+=1
        
        return result