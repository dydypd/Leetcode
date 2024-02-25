class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1
        
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]
        
        dp = [[0] * n for _ in range(n)]
        for l in range(k, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i][j] = sys.maxsize
                for m in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j])
                if (l - 1) % (k - 1) == 0:
                    dp[i][j] += prefix_sum[j + 1] - prefix_sum[i]
        
        return dp[0][n - 1]