n = int(input())
a = list(map(int, input().split()))
re_a = a[::-1]

up = [1 for _ in range(n)]
down = [1 for _ in range(n)]
dp = [0 for _ in range(n)]

for i in range(n) :
    for j in range(i) :
        if a[i] > a[j] :
            up[i] = max(up[i], up[j]+1)
        if re_a[i] > re_a[j] :
            down[i] = max(down[i], down[j]+1)
        
for i in range(n) :
    dp[i] = up[i] + down[n-i-1] - 1
    
print(max(dp))