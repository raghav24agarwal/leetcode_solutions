class Solution(object):
    def isPalindrome(self, x):
        
        if x<0:
            return False
        
        #without converting it to string
        
        num = x
        divisor = 1
        while(x>=10):
            x=x//10
            divisor*=10
            
        print(divisor)
        
        while(num>0):
            
            first = num//divisor
            last = num%10
            
            if first!=last:
                return False
            
            #remove the digits from both side
            num = (num%divisor)//10
            
            divisor = divisor//100
            
        return True
                
        
        
        