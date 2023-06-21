# https://www.acmicpc.net/problem/1697

from collections import deque

n, k = map(int, input().split())

bfsQueue = deque()
MAX = 10
visited = [0 for _ in range(MAX + 1)]

def bfs():    
    while bfsQueue:
        loc = bfsQueue.popleft()

        if loc == k:
            print(visited[loc])
            break

        for nloc in (loc - 1, loc + 1, loc * 2):
            if 0 <= nloc <= MAX and not visited[nloc]:
                visited[nloc] = visited[loc] + 1
                bfsQueue.append(nloc)

            print(visited)

bfsQueue.append(n)
bfs()

