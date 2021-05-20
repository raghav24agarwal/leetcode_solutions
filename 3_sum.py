class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        if n==0:
            return []
        
        res = set()
        
        i = 0
        
        for i in range(0,n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
                
            left = i+1
            right = n-1
            
            while(left<right):
                
                summ = nums[i]+nums[left]+nums[right]
                
                if summ==0:
                    
                    res.add((nums[i],nums[left],nums[right]))
                    left+=1
                    
                elif summ>0:
                    right-=1
                    
                else:
                    left+=1
            
            
        result = []
        
        for i in res:
            result.append(list(i))
        return result
                
                
                
        