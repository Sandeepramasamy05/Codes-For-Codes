class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1  # Day 1: one person knows the secret

        for i in range(2, n + 1):
            # Count people who can share on day i
            for j in range(max(1, i - forget + 1), i - delay + 1):
                dp[i] = (dp[i] + dp[j]) % MOD

        # Count people who still remember the secret on day n
        result = 0
        for j in range(n - forget + 1, n + 1):
            if j >= 1:
                result = (result + dp[j]) % MOD

        return result
