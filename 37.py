class Solution:
    
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(row: int, col:int, num:int):
            for i in range(9):
                if board[i][col] == num or board[row][i] == num:
                    return False
                if  board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                    return False
            return True
        
        def solve(row:int, col:int):
            if col == 9:
                return True
            if row == 9:
                return solve(0, col + 1)
            
            if board[row][col] == ".":
                possibilities = [num for num in map(str, range(1, 10)) if isValid(row, col, num)]
                for num in possibilities:
                    board[row][col] = num
                    if solve(row + 1, col):
                        return True
                    else:
                        board[row][col] = "."
                return False
            else:
                return solve(row +1, col)
        
        solve(0,0)
