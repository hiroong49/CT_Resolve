# combination으로 풀기
from itertools import combinations

n, m = list(map(int, input().split()))
card = list(map(int, input().split()))

jack = combinations(card, 3)
ans = []

for i in jack:
    if sum(i) <= m:
        ans.append(sum(i))
        
print(max(ans))

# 브루트포스
n, m = list(map(int, input().split()))
card = list(map(int, input().split()))

jack = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            combi = card[i] + card[j] + card[k]

            if combi > m:
                continue
            else:
                jack = max(jack, combi)
        
print(jack)

