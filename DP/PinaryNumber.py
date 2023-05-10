n = int(input())

dp = [1 for _ in range(91)]

for i in range(3, 91) :
    dp[i] = dp[i-1] + dp[i-2]
        
print(dp[n])