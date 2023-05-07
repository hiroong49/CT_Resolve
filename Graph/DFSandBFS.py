from collections import deque

n, m, v = map(int, input().split())

adjList = [[] for _ in range(n+1)]
bfsQueue = deque([])
# visited 배열 - bool
visited = [False for _ in range(n+1)] 


for i in range(m):
    f, t = map(int, input().split())
    
    adjList[f].append(t)
    adjList[t].append(f)
    
# dfs - Recursion
def dfs(num) :
    print(num, end = ' ')
    for element in adjList[num] :
        if visited[element] :
            continue
        visited[element] = True
        dfs(element)
    
# bfs - Queue
def bfs() :
    while bfsQueue :
        currentNumber = bfsQueue.popleft()
        print(currentNumber, end=' ')
        for element in adjList[currentNumber] :
            if visited[element] :
                continue
            visited[element] = True
            bfsQueue.append(element)
            
def clearVisited() :
    global visited
    visited = [False for _ in range(n+1)] 
            
# sort
for i in range(n+1):
    adjList[i].sort()
    
# dfs
visited[v] = True
dfs(v)
print()

# visited 배열 초기화
clearVisited()
            
# bfs - 방문 처리랑 큐에 출발 노드 넣기
visited[v] = True
bfsQueue.append(v)
bfs()