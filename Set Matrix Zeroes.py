'''
Set Matrix Zeroes: Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to
0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1

Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

class Solution:
    def setZeros(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zeros = False

        # Check if first row has zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True

        # Check if first column has zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zeros = True

        # Use first row and column to mark zeros
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0  # <-- fixed assignment

        # Set cells to 0 based on marks
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Set first row to 0
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Set first column to 0
        if first_col_zeros:
            for i in range(m):
                matrix[i][0] = 0

# Test the code
sol = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(matrix)
sol.setZeros(matrix)
print(matrix)