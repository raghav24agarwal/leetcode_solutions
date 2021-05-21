class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        
        def backtracking(open_bracket,closed_bracket,string):
            if open_bracket==closed_bracket==n:
                result.append(string)
                return
            
            if open_bracket<n:
                backtracking(open_bracket+1,closed_bracket,string+"(")
                
            if closed_bracket<open_bracket:
                backtracking(open_bracket,closed_bracket+1,string+")")
                
                
        backtracking(0,0,"")
        
        return result
        