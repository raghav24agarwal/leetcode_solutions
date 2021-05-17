class Solution:
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        length = len(nums)
        nums.sort()
        res = set()
        
        i=0
        while(i<=length-4):

            #skipping duplicate elements for i
            if i>0 and (nums[i]==nums[i-1]):
                i+=1
                continue
                
            j = i+1
            while(j<=length-3):

                #skipping duplicate elements for j
                if j>i+1 and nums[j]==nums[j-1]:
                    j+=1
                    continue
                    
                left = j+1
                right = length-1
                
                while(left<right):
                    
                    summ = nums[i]+nums[j]+nums[left]+nums[right]
                    if summ==target:
                        t = (nums[i],nums[j],nums[left],nums[right])
                        res.add(t)
                        left+=1
                        
                    elif summ<target:
                        left+=1

                    else:
                        right-=1

                            
                j+=1
            
            i+=1
                            
        result = []
        for i in res:
            temp = list(i)
            result.append(temp)
            
        return result
                        
        