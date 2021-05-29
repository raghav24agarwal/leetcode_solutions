class Solution:
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        #for first column
        for i in range(1,rows):
            grid[i][0] += grid[i-1][0]
            
        #for first row
        for j in range(1,cols):
            grid[0][j] += grid[0][j-1]
            
        #for rest of the grid
        for i in range(1,rows):
            for j in range(1,cols):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        
        return grid[rows-1][cols-1]
        