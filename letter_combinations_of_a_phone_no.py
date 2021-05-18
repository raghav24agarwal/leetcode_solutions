class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        
        length = len(digits)
        if length==0:
            return []
        
        keypad = {  "2":"abc",
                    "3":"def",
                    "4":"ghi",
                    "5":"jkl",
                    "6":"mno",
                    "7":"pqrs",
                    "8":"tuv",
                    "9":"wxyz"
                 }
        
        result = []
        
        def backtracking(index,digits,string):
            if len(string)==len(digits):
                result.append(string)
                return
                
            for i in keypad[digits[index]]:
                string = string+i
                backtracking(index+1,digits,string)
                string = string[:-1]

                
        backtracking(0,digits,"")
        
        return result
                
        