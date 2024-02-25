class Solution:
    def totalNQueens(self, n: int) -> int:
        def isSafe(board, row, col):
            for i in range(col):
                if board[i] == row or \
                board[i] - i == row - col or \
                board[i] + i == row + col:
                    return False
            return True

        def solve(board, col):
            if col == n:
                return 1
            count = 0
            for i in range(n):
                if isSafe(board, i, col):
                    board[col] = i
                    count += solve(board, col + 1)
            return count

        return solve([-1] * n, 0)
