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
