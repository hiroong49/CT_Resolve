# https://www.acmicpc.net/problem/5014

from collections import deque

f, s, g, u, d = map(int, input().split())

queue = deque([])
visited = [0 for _ in range(f+1)]

def bfs():
    while queue:
        loc = queue.popleft()
        if loc == g:
            return visited[loc] - 1
        for nloc in (loc + u, loc - d):
            if 0 < nloc <= f and not visited[nloc]:
                visited[nloc] = visited[loc] + 1
                queue.append(nloc)

    return 'use the stairs'

queue.append(s)
visited[s] = 1
print(bfs())