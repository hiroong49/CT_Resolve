t = int(input())

dp = [1 for _ in range(101)]

for _ in range(t):
    n = int(input())

    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2]

    print(dp[n])
