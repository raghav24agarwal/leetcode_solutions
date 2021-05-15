class Solution:
    def reverse(self, x: int) -> int:
        
        maxx = (2**31)-1
        minn = -(2**31)
        
        result = 0
        
        x2 = x
        
        x = abs(x)
        
        while(x>0):
            
            mod = x%10
            x = x//10
            
            result = (result*10)+mod
            
        if x2<0:
            result = -result
            
        if result>maxx or result<minn:
            return 0
        
        return result
    