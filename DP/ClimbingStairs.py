n = int(input())

st = [0 for _ in range(301)]
dp = [0 for _ in range(301)]

for i in range(n):
    st[i] = int(input())

dp[0] = st[0]
dp[1] = st[0] + st[1]
dp[2] = max(st[0] + st[2], st[1] + st[2])

for i in range(3, n):
    # 1) 전 계단을 밟은 경우와 2) 전 계단을 밟지 않은 경우로 나눌 수 있음
    # ex) dp[3] = st[0] + st[1] + st[3], st[0] + st[2] + st[3] 중 더 큰 값
    dp[i] = max(dp[i-2] + st[i], dp[i-3] + st[i-1] + st[i])

print(dp[n-1])