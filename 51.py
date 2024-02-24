class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def isSafe(board, row, col):
            for i in range(col):
                if board[row][i] == 'Q':
                    return False

            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False

            for i, j in zip(range(row, n, 1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False

            return True

        def solve(board, col):
            if col >= n:
                solutions.append([''.join(row) for row in board])
                return

            for i in range(n):
                if isSafe(board, i, col):
                    board[i][col] = 'Q'
                    solve(board, col + 1)
                    board[i][col] = '.' 
        board = [['.' for _ in range(n)] for _ in range(n)]
        solutions = []
        solve(board, 0)
        return solutions
 
test = Solution()

print(test.solveNQueens(8))
