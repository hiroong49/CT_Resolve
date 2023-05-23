n = int(input())
ans = []

for i in range(n) :
    age, name = map(str, input().split())
    ans.append([int(age), i, name])

ans.sort()

for i in range(n) :
    print(ans[i][0], ans[i][2])