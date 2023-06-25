# https://www.acmicpc.net/problem/7569

from collections import deque

m, n, h = map(int, input().split())

dy = [-1, 0, 1, 0, 0, 0]
dx = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

adjMatrix = []
bfsQueue = deque([])
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)] 

cnt = 0

for i in range(h):
    arr = []
    for j in range(n):
        arr.append(list(map(int, input().split())))
    adjMatrix.append(arr)

def bfs():
    while bfsQueue:
        curY, curX, curZ = bfsQueue.popleft()
        for i in range(6):
            ny = curY + dy[i]
            nx = curX + dx[i]
            nz = curZ + dz[i]
            if ny < 0 or nx < 0 or nz < 0 or ny >= h or nx >= n or nz >= m:
                continue
            if visited[ny][nx][nz] != 0:
                continue
            if adjMatrix[ny][nx][nz] == -1:
                continue
            bfsQueue.append((ny, nx, nz))
            visited[ny][nx][nz] = 1
            adjMatrix[ny][nx][nz] = adjMatrix[curY][curX][curZ] + 1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if adjMatrix[i][j][k] == 1 and visited[i][j][k] == 0:
                bfsQueue.append((i, j, k))
                visited[i][j][k] = 1

bfs()

for i in adjMatrix:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
        cnt = max(cnt, max(j))

print(cnt-1)
