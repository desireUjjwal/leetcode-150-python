# 73. Set Matrix Zeroes

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

class Solution(object):
    def setZeroes(self, matrix):
        rows = [1] * len(matrix)
        cols = [1] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    cols[j] = 0

        for i in range(len(matrix[0])):
            if cols[i] == 0:
                for j in range(len(matrix)):
                    matrix[j][i] = 0

        for i in range(len(matrix)):
            if rows[i] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0

# Using Constant extra space
class Solution(object):
    def setZeroes(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

