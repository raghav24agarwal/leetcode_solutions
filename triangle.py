class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        if len(triangle)==1:
            return triangle[0][0]
        
        rows = len(triangle)
        
        for i in range(1,rows):
            for j in range(i+1):
                
                if j==0:
                    triangle[i][j] += triangle[i-1][j]
                    
                elif j==i:
                    triangle[i][j] += triangle[i-1][j-1]
                    
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
                    
                    
        return(min(triangle[-1]))