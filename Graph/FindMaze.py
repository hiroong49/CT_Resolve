from collections import deque

n, m = map(int, input().split())

adjMatrix = []
visited = [[0 for _ in range(m+1)] for _ in range(n+1)]

bfsQueue = deque([])
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(n):
    adjMatrix.append(list(map(int, input())))

# bfs - Queue
def bfs() :
    while bfsQueue :
        currentLocation = bfsQueue.popleft()
        curY = currentLocation[0]
        curX = currentLocation[1]
        for i in range(4) :
            ny = curY + dy[i]
            nx = curX + dx[i]
            # (0, 0), (n-1, m-1) 일 때 넘어가면 패스
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            # 0 은 벽이라서 이동할 수 없음
            if adjMatrix[ny][nx] == 0 :
                continue
            # 이미 방문한 곳이면 패스
            if visited[ny][nx] != 0 :
                continue
            visited[ny][nx] = visited[curY][curX] + 1
            bfsQueue.append((ny, nx))

# bfs - 방문 처리, 큐, 호출
visited[0][0] += 1
bfsQueue.append((0, 0))
bfs()
print(visited[n-1][m-1])
        