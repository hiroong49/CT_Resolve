# https://www.acmicpc.net/problem/14891

from collections import deque

wheel = []
score = 0

def left(start, dirs):
    if start < 0:
        return
    if wheel[start][2] != wheel[start+1][6]:
        left(start-1, -dirs)
        wheel[start].rotate(dirs)

def right(start, dirs):
    if start > 3:
        return
    if wheel[start][6] != wheel[start-1][2]:
        right(start+1, -dirs)
        wheel[start].rotate(dirs)

for _ in range(4):
    wheel.append(deque(list(input())))

k = int(input())

for _ in range(k):
    num, dir = map(int, input().split())
    num -= 1

    left(num-1, -dir) # 왼쪽 조사
    right(num+1, -dir) # 오른쪽 조사
    wheel[num].rotate(dir)

if wheel[0][0] == '1':
    score += 1
if wheel[1][0] == '1':
    score += 2
if wheel[2][0] == '1':
    score += 4
if wheel[3][0] == '1':
    score += 8

print(score)