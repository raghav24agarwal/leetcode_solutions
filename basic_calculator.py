class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        length = len(s)
        result = 0
        i = 0
        sign = 1
        
        while i<length :
            if s[i] in "1234567890" :
                num = 0
                j=i
                while(j<length) and s[j] in "1234567890" :
                    num = (num*10) + int(s[j])
                        
                    j+=1
                i = j
                i -= 1
                
                result = result + (sign*num)
                
            elif s[i] == " " :
                pass
                
            elif s[i] == "+" :
                sign = 1
                
            elif s[i] == "-" :
                sign = -1
                
            elif s[i] == "(" :
                
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
                
            elif s[i] == ")" :
                
                result = result * stack.pop()
                result = result + stack.pop()
                
            i+=1
                
        return result
        