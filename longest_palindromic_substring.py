class Solution(object):
    def longestPalindrome(self, s):
        
        length = len(s)

        maxpalsize = 1
        maxpal = s[0]
        dp = [[0 for i in range (length+1)] for j in range (length+1)]
        
        #strings of length one are always palindrome
        for i in range(0,length+1):
            dp[i][i] = 1
        
        #strings of length two are palindrome if both the letters are same
        for i in range(0,length-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = 1
                maxpalsize = 2
                maxpal = s[i:i+2]
        
        #for strings of length greater than two
        k = 2
        while(k<length):
            i=0
            j=k
            while(j<length):
                if dp[i+1][j-1]==1 and s[i]==s[j]:
                    dp[i][j]=1
                    
                    maxpalsize = k+1
                    maxpal = s[i:j+1]
                    
                    
                i+=1
                j+=1
            
            k+=1
            
        return maxpal
                
                
                
            