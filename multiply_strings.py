class Solution:
    
    def multiply(self, num1: str, num2: str) -> str:
        
        n1, n2 = len(num1), len(num2)
        result = [0] * (n1+n2) 
        index2 = 0
        
        for i in range(n2-1,-1,-1):  
            carry = 0
            digit1 = ord(num2[i]) - 48
            
            index1 = 0
            
            for j in range(n1-1,-1,-1):
                digit2 = ord(num1[j]) - 48
                
                multiply = (digit1*digit2) + carry +result[index1+index2]
                val = multiply%10
                carry = multiply//10
                
                result[index1 + index2] = val
                if result[index1+index2] >= 10:
                    
                    temp = result[index1 + index2]
                    result[index1 + index2] = temp%10
                    
                    result[index1+index2+1] += temp//10
                    
                
                index1 += 1
                
            if carry!=0:
                result[index1+index2] += carry
                
            index2+=1
            
        
        length = len(result)
        
        for k in range(length-1,-1,-1):
            if result[k]==0:
                result.pop()
            else:
                break
                
        result = result[::-1]
        
        string = ""
        for ele in result:
            string += chr(ele+48)
        
        if len(string)==0:
            return "0"
        
        return string