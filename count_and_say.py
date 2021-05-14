class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n==1:
            return "1"
        elif n==2:
            return "11"
        
        string = "11"
        
        for i in range(3,n+1):
            
            result = ""
            count = 1
            j=0
            
            while(j<len(string)-1):
                if string[j]==string[j+1]:
                    count+=1
                else:
                    result = result + str(count) + str(string[j])
                    count = 1
                    
                j+=1
                
            result = result + str(count) + str(string[j])

            string = result
            

        return result
        
        