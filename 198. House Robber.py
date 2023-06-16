def rob(nums):
    dp = [0]*len(nums)
    dp[0] = nums[0]  # base cases
    dp[1] = nums[1]

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])

    return dp[-1]
