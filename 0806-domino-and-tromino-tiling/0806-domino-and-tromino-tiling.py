MOD = int(1e9 + 7)
class Solution:
    def numTilings(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] % MOD + dp[i - 3] % MOD) % MOD
        return dp[n]