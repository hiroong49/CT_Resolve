from collections import deque

n = int(input())
con = int(input())

adjList = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)] 

bfsQueue = deque([])
cnt = 0

for i in range(con) :
    f, t = map(int, input().split())
    adjList[f].append(t)
    adjList[t].append(f)
    
# bfs - Queue
def bfs() :
    global cnt
    while bfsQueue :
        currentNumber = bfsQueue.popleft()
        for element in adjList[currentNumber] :
            if visited[element] :
                continue
            visited[element] = True
            bfsQueue.append(element)
            cnt += 1
    return cnt
            
# bfs - 방문 처리, 큐에 넣기, 함수 호출
visited[1] = True
bfsQueue.append(1)
print(bfs())