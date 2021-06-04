class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        
        visited = [ [0 for i in range(cols) ] for j in range(rows) ]
        
        def dfs(index, i, j, board, word):
            if index==len(word):
                return True
            
            if i<0 or i>rows-1 or j<0 or j>cols-1 or board[i][j]!=word[index] or visited[i][j]==1:
                return False
            
            visited[i][j] = 1
            
            if dfs(index+1, i+1, j, board, word) or dfs(index+1, i-1, j, board, word) or dfs(index+1, i, j+1, board, word) or dfs(index+1, i, j-1, board, word):
                return True
            
            visited[i][j] = 0
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(0, i, j, board, word):
                    return True
                
            
        return False