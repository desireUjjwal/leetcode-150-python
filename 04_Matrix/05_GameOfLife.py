# 89. Game of Life

# According to Wikipedia's article: "The Game of Life, also known simply as Life,
# is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0).
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# 1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
# 2. Any live cell with two or three live neighbors lives on to the next generation.
# 3. Any live cell with more than three live neighbors dies, as if by over-population.
# 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process,
# births and deaths occur simultaneously.

# Given the current state of the board, update the board to reflect its next state.

# Note that you do not need to return anything.

import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        newBoard = copy.deepcopy(board)

        for r in range(ROWS):
            for c in range(COLS):
                delRow = [-1, 0, 1]
                delCol = [-1, 0, 1]

                count = 0
                for i in range(3):
                    for j in range(3):
                        nRow = r + delRow[i]
                        nCol = c + delCol[j]
                        if((nRow >= 0 and nRow < ROWS) and (nCol >= 0 and nCol < COLS)):
                            if nRow == r and nCol == c:
                                continue
                            if(board[nRow][nCol] == 1):
                                count += 1
                if board[r][c] == 1:
                    if count == 2 or count == 3:
                        newBoard[r][c] = 1
                    elif count < 2:
                        newBoard[r][c] = 0
                    else:
                        newBoard[r][c] = 0
                if board[r][c] == 0:
                    if count == 3:
                        newBoard[r][c] = 1
        for r in range(ROWS):
            for c in range(COLS):
                board[r][c] = newBoard[r][c]
