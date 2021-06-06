class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows, cols = len(matrix), len(matrix[0])
        
        #This solution has been done in constant space
        #using first row and first column for deciding which rows and columns
        #should be zero
        
        #using one extra variable for first row
        #because first cell is common in first row and column
        first_row = 1
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    #for column
                    matrix[0][j] = 0
                    
                    #for row
                    if i==0:
                        first_row = 0
                    else:
                        matrix[i][0] = 0
        
        #checking for rows except first row
        for i in range(1,rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] = 0
                    
        #checking for columns except first column
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0
                    
        #for first column
        if matrix[0][0] == 0:
            for i in range(rows):
                matrix[i][0] = 0
                
        #for first row
        if first_row == 0:
            for j in range(cols):
                matrix[0][j] = 0
                
        #print(matrix)