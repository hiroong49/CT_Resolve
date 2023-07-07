# https://www.acmicpc.net/problem/2644

from collections import deque

n = int(input())

a, b = map(int, input().split())
m = int(input())

queue = deque([])
adjList = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

def bfs():
    while queue:
        curNum = queue.popleft()
        for element in adjList[curNum]:
            if visited[element] == 0:
                visited[element] = visited[curNum] + 1
                queue.append(element)

for _ in range(m):
    x, y = map(int, input().split())

    adjList[x].append(y)
    adjList[y].append(x)

queue.append(a)
bfs()

if visited[b] > 0:
    print(visited[b])
else:
    print(-1)
