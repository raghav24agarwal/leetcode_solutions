class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        
        #converting first cell of each row to 1
        for i in range(rows):
            if grid[i][0] == 0:
                
                #flip that row
                
                for j in range(cols):
                    
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
                        
                        
        #flipping the columns which has less no of 1's than 0's
        for j in range(1,cols):
            col_sum = 0
            for i in range(rows):
                col_sum+=grid[i][j]
                
            if rows-col_sum>col_sum:
                
                #flip that column
                
                for i in range(rows):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
                        

        #converting each row to binary and then to int
        result = 0
        for i in range(rows):
            result += int("".join(str(j) for j in (grid[i])),2)

        return result