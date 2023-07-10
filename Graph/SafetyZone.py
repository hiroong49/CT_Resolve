# https://www.acmicpc.net/problem/2468

from collections import deque

n = int(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

adjMatrix = []
queue = deque()

maxNum = 0
value = 0

def bfs():
    while queue:
        curY, curX = queue.popleft()
        for i in range(4):
            ny = curY + dy[i]
            nx = curX + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if adjMatrix[ny][nx] > value and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))


for i in range(n):
    adjMatrix.append(list(map(int, input().split())))

    for j in range(n):
        if adjMatrix[i][j] > maxNum:
            maxNum = adjMatrix[i][j]

result = 0

for i in range(maxNum):
    visited = [[0 for _ in range(n)] for _ in range(n)]

    cnt = 0

    for j in range(n):
        for k in range(n):
            if adjMatrix[j][k] > i and visited[j][k] == 0:
                queue.append((j, k))
                visited[j][k] = 1
                value = i
                bfs()
                cnt += 1
        
    if result < cnt:
        result = cnt

print(result)