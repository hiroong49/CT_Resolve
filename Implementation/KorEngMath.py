import sys

n = int(sys.stdin.readline())
ans = []

for i in range(n):
    name, kor, eng, math = map(str, sys.stdin.readline().split())
    ans.append([name, int(kor), int(eng), int(math)])

ans.sort(key = lambda x:(-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(ans[i][0])