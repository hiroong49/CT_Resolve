# https://www.acmicpc.net/problem/15662

from collections import deque

wheel = []
cnt = 0

def left(start, dirs):
    if start < 0:
        return
    if wheel[start][2] != wheel[start+1][6]:
        left(start-1, -dirs)
        wheel[start].rotate(dirs)

def right(start, dirs):
    if start > t - 1:
        return
    if wheel[start][6] != wheel[start-1][2]:
        right(start+1, -dirs)
        wheel[start].rotate(dirs)

t = int(input())

for _ in range(t):
    wheel.append(deque(input()))

k = int(input())

for _ in range(k):
    num, dir = map(int, input().split())
    num -= 1

    left(num-1, -dir)
    right(num+1, -dir)
    wheel[num].rotate(dir)

for i in range(t):
    if wheel[i][0] == '1':
        cnt += 1

print(cnt)