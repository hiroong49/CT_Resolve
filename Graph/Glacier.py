# https://www.acmicpc.net/problem/2573

from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())

adjMatrix = []
queue = deque()

day = 0

def bfs():
    while queue:
        curY, curX = queue.popleft()
        for i in range(4):
            ny = curY + dy[i]
            nx = curX + dx[i]
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0:
                if adjMatrix[ny][nx] != 0:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))
                elif adjMatrix[ny][nx] == 0:
                    cnt[curY][curX] += 1

for _ in range(n):
    adjMatrix.append(list(map(int, input().split())))

while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    cnt = [[0 for _ in range(m)] for _ in range(n)]
    result = []

    for i in range(n):
        for j in range(m):
            if adjMatrix[i][j] != 0 and visited[i][j] == 0:
                queue.append((i, j))
                visited[i][j] = 1
                result.append(bfs())

    for i in range(n):
        for j in range(m):
            adjMatrix[i][j] -= cnt[i][j]
            if adjMatrix[i][j] < 0:
                adjMatrix[i][j] = 0

    if len(result) == 0:
        print(0)
        break
    if len(result) >= 2:
        print(day)
        break

    day += 1