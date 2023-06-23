# https://www.acmicpc.net/problem/7562

from collections import deque

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

t = int(input())

def bfs():
    while queue:
        curX, curY = queue.popleft()
        if curX == desx and curY == desy:
            return visited[desx][desy] - 1
        for i in range(8):
            nx = curX + dx[i]
            ny = curY + dy[i]
            if 0 <= ny < l and 0 <= nx < l and visited[nx][ny] == 0:
                visited[nx][ny] = visited[curX][curY] + 1
                queue.append((nx, ny))

for _ in range(t):
    l = int(input())
    x, y = map(int, input().split())
    desx, desy = map(int, input().split())
    
    queue = deque()
    visited = [[0 for _ in range(l)] for _ in range(l)]
    
    queue.append((x, y))
    visited[x][y] = 1
    print(bfs())