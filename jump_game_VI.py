class Solution:
    
    def maxResult(self, nums: List[int], k: int) -> int:
        
        cost = nums[0]
        length = len(nums)
        
        #inserting first index in decreasing deque
        dec_queue = deque([0])
        
        for i in range(1,length):
            
            #if the difference of current index and maximum index value in the deque
            #is greater than k
            #then, we remove that index
            if i - dec_queue[0] > k:
                dec_queue.popleft()
                
            nums[i] += nums[dec_queue[0]]
            
            #maintaining the decreasing queue
            while len(dec_queue) and nums[i]>nums[dec_queue[-1]]:
                dec_queue.pop()
                
            dec_queue.append(i)
            
        #print("nums",nums)
        
        return nums[-1]