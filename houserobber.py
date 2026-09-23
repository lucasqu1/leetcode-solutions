class Solution:
    def houserobber(self, nums: list[int]) -> int:
        # dp[1][i] = the amount of money we make taking from house i, (houses 1 to i)
        # dp[0][i] = the amount of money we make skipping house i, (houses 1  to i)
        # dp[1][i] = dp[0][i - 1] + nums[i]
        # dp[0][i] = max(dp[0][i - 1], dp[1][i - 1])
        # answer should be max(dp[1][n - 1], dp[0][n - 1]
        # 1 2 3 4
        n = len(nums)
        dp = [[0 for i in range(n)] for j in range(2)]

        dp[1][0] = nums[0]
        dp[0][0] = 0

        for i in range(n):
          if i == 0:
            continue

          dp[1][i] = dp[0][i - 1] + nums[i]
          dp[0][i] = max(dp[0][i - 1], dp[1][i - 1])

        return max(dp[1][n - 1], dp[0][n - 1])

        # This recurrence works because we never rob adjacent houses.
        # additionally you can do a very simple proof of induction to show this recurrence is optimal
