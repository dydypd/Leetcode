class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        def is_magic(i, j):
            s = "".join(str(grid[i + x // 3][j + x % 3]) for x in [0, 1, 2, 5, 8, 7, 6, 3])
            return grid[i][j] == 5 and "".join(sorted(s)) == "123456789"

        return sum(is_magic(i, j) for i in range(len(grid) - 2) for j in range(len(grid[0]) - 2))
