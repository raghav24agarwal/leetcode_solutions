class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def first(nums:List[int], target:int, n:int) -> int:
            
            l = 0
            r = n-1
            firstpos = -1
            
            while(l<=r):
                
                mid = (l+r)//2
                
                if nums[mid]==target:
                    firstpos = mid
                    if mid!=0 and nums[mid-1]!=target:
                        break
                    r = mid-1
                    
                elif nums[mid]<target:
                    l = mid+1
                    
                else:
                    r = mid-1
                    
            return firstpos
        
        def last(nums:List[int], target:int, n:int) -> int:
            
            l = 0
            r = n-1
            lastpos = -1
            
            while(l<=r):
                
                mid = (l+r)//2
                
                if nums[mid]==target:
                    lastpos = mid
                    if mid!=n-1 and nums[mid+1]!=target:
                        break
                    l = mid+1
                    
                elif nums[mid]<target:
                    l = mid+1
                    
                else:
                    r = mid-1
                    
            return lastpos
        
        length = len(nums)
        firstpos = first(nums,target,length)
        lastpos = last(nums,target,length)
        
        ans = [firstpos,lastpos]
        return ans
        



