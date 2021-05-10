class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dic = {}
        result = []
        len1 = len(nums)
        
        for i in range(0,len1):
            if target-nums[i] in dic:
                result.extend([dic[target-nums[i]],i])
                
            else:
                dic[nums[i]] = i
                
            
        return result
                

        