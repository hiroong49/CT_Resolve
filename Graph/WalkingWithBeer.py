# https://www.acmicpc.net/problem/9205

from collections import deque

t = int(input())

def bfs():
    queue = deque()
    queue.append([home[0], home[1]])
    while queue:
        curX, curY = queue.popleft()
        if abs(curX - fest[0]) + abs(curY - fest[1]) <= 1000:
            return 'happy'
        
        for element in range(n):
            if not visited[element]:
                nx, ny = adjList[element]
                if abs(curX - nx) + abs(curY - ny) <= 1000:
                    queue.append([nx, ny])
                    visited[element] = 1

    return 'sad'

for _ in range(t):
    n = int(input())
    adjList = []

    home = [int(x) for x in input().split()]

    for _ in range(n):
        x, y = map(int, input().split())
        adjList.append([x, y])

    fest = [int(x) for x in input().split()]

    visited = [0 for _ in range(n+1)]
    print(bfs())