n = int(input())
con = int(input())

adjList = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
cnt = 0

for i in range(con) :
    f, t = map(int, input().split())
    adjList[f].append(t)
    adjList[t].append(f)
    
# dfs - Recursion. 매개변수
def dfs(num) :
    global cnt
    for element in adjList[num] :
        if visited[element] :
            continue
        visited[element] = True
        dfs(element)
        cnt += 1
    return cnt

# dfs - visited 처리, dfs(인자) 호출 
visited[1] = True
print(dfs(1))