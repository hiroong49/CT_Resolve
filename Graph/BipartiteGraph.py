# 이분 그래프
# https://www.acmicpc.net/problem/1707

from collections import deque
import sys

k = int(sys.stdin.readline())

def bfs(start):
    visited[start] = 1
    bfsQueue = deque([start])
    while bfsQueue:
        curNum = bfsQueue.popleft()
        for element in adjList[curNum]:
            # 방문하지 않은 노드라면, 큐에 추가하고 상위 노드와 다른 그룹으로 편성
            if visited[element] == 0:
                bfsQueue.append(element)
                visited[element] = -visited[curNum]
            # 만약 이미 방문한 노드인데 같은 그룹이라면 False 리턴
            elif visited[element] == visited[curNum]:
                return False
    return True

for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())

    adjList = [[] for _ in range(v+1)]
    visited = [0 for _ in range(v+1)]

    for _ in range(e):
        f, t = map(int, sys.stdin.readline().split())
        adjList[f].append(t)
        adjList[t].append(f)

    flag = True

    for i in range(1, v+1):
        # 방문하지 않았다면 bfs 호출
        if visited[i] == 0:
            result = bfs(i)
            if not result:
                flag = False
                break
    
    if flag:
        print('YES')
    else:
        print('NO')