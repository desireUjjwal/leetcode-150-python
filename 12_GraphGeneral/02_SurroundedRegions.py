# 130. Surrounded Regions

# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.n = len(board)
        self.m = len(board[0])
        self.visited = []
        for _ in range(self.n):
            row = [False] * self.m
            self.visited.append(row)

        for j in range(self.m):
            if self.visited[0][j] == False and board[0][j] == 'O':
                self.dfs(board, 0, j)
            if self.visited[self.n-1][j] == False and board[self.n-1][j] == 'O':
                self.dfs(board, self.n-1, j)
        
        for i in range(self.n):
            if self.visited[i][0] == False and board[i][0] == 'O':
                self.dfs(board, i, 0)
            if self.visited[i][self.m-1] == False and board[i][self.m-1] == 'O':
                self.dfs(board, i, self.m-1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.visited[i][j] == False and board[i][j] == 'O':
                    board[i][j] = 'X'

        
    def dfs(self, board: List[List[str]], i: int, j: int) -> None:
        if i < 0 or j < 0 or i >= self.n or j >= self.m or self.visited[i][j] == True or board[i][j] == 'X':
            return
        self.visited[i][j] = True
        self.dfs(board, i+1, j)
        self.dfs(board, i-1, j)
        self.dfs(board, i, j+1)
        self.dfs(board, i, j-1)





    
