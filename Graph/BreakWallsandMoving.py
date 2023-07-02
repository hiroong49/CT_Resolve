# 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206

from collections import deque

n, m = map(int, input().split())

dy = [-1, 0 , 1, 0]
dx = [0, 1, 0, -1]

adjMatrix = []
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
queue = deque([])

for _ in range(n):
    adjMatrix.append(list(map(int, input())))

def bfs():
    while queue:
        curY, curX, curZ = queue.popleft()
        if curY == n-1 and curX == m-1:
            return visited[curY][curX][curZ]
        for i in range(4):
            ny = curY + dy[i]
            nx = curX + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if adjMatrix[ny][nx] == 1 and curZ == 0:
                visited[ny][nx][1] = visited[curY][curX][0] + 1
                queue.append((ny, nx, 1))
            if adjMatrix[ny][nx] == 0 and visited[ny][nx][curZ] == 0:
                visited[ny][nx][curZ] = visited[curY][curX][curZ] + 1
                queue.append((ny, nx, curZ))
    return -1

visited[0][0][0] = 1
queue.append((0, 0, 0))
print(bfs())