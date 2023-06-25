# https://www.acmicpc.net/problem/16928

from collections import deque

n, m = map(int, input().split())

ladder = {}
snakes = {}

answer = [0 for _ in range(101)]
queue = deque([1])
visited = [0 for _ in range(101)]

# 사다리 정보 저장
for _ in range(n):
    x, y = map(int, input().split())

    ladder[x] = y

# 뱀 정보 저장
for _ in range(m):
    u, v = map(int, input().split())

    snakes[u] = v

def bfs():
    while queue:
        pos = queue.popleft()
        if pos == 100:
            print(answer[pos])
            break
        for i in range(6):
            nloc = pos + i + 1
            if nloc > 100 or nloc < 0:
                continue
            if nloc in ladder.keys():
                nloc = ladder[nloc]
            if nloc in snakes.keys():
                nloc = snakes[nloc]
            if not visited[nloc]:
                queue.append(nloc)
                visited[nloc] = 1
                answer[nloc] = answer[pos] + 1

visited[1] = 1
bfs()
