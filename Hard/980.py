class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start, end = None, None
        obstacles = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == -1:
                    obstacles.add((i, j))

        def dfs(x, y, visited):
            if (x, y) == end:
                return 1 if len(visited) == m * n - len(obstacles) else 0

            count = 0
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and (nx, ny) not in obstacles:
                    count += dfs(nx, ny, visited | {(nx, ny)})

            return count

        return dfs(start[0], start[1], {start})