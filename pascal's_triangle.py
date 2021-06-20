class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows==1:
            return [[1]]
        
        if numRows==2:
            return [[1],[1,1]]
        
        result = []
        
        for i in range(1,numRows+1):
                l = [1]*i
                result.append(l)
        
        for i in range(2,numRows):
            for j in range(1,i):
                result[i][j] = result[i-1][j-1]+result[i-1][j]
                
        return(result)