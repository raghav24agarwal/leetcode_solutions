class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        n = len(strs)
        
        if n==0:
            return ""
        elif n==1:
            return strs[0]
        
        prefix = strs[0]
        prefix_len = len(prefix)
        length = 200
        
        for st in range(1,n):
            
            minn = min(prefix_len,len(strs[st]))
            
            i = 0

            count = 0
            
            while(i<minn):
                if prefix[i]==strs[st][i]:
                    count+=1
                    i+=1
                else:
                    break
                    
            length = min(length,count)
        
        return prefix[0:length]
                