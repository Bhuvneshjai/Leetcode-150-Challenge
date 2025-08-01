'''
Game of Life: According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular
automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1)
or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using
the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the
current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.

Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
'''

class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        rows, cols = len(board), len(board[0])

        # Copy the original board
        copy = [row[:] for row in board]

        # Directions for the 8 neighbors
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0),  (1, 1)]

        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0

                # Count live neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if copy[nr][nc] == 1:
                            live_neighbors += 1

                # Apply the rules using the copy, and write to original board
                if copy[r][c] == 1:  # cell is alive
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 0  # dies
                else:  # cell is dead
                    if live_neighbors == 3:
                        board[r][c] = 1  # becomes alive

board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]

sol = Solution()
sol.gameOfLife(board)

# Output the updated board
for row in board:
    print(row)
