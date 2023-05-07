n = int(input())

adjMatrix = []
visited = [[0 for _ in range(n+1)] for _ in range(n+1)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

apartCnt = 0
danji = 0
ans = []

for i in range(n) :
    adjMatrix.append(list(map(int, input())))
    
# dfs(num) - Recursion
def dfs(y, x) :
    global apartCnt
    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= n or nx >= n :
            continue
        if adjMatrix[ny][nx] == 0 :
            continue
        if visited[ny][nx] != 0 :
            continue
        visited[ny][nx] = 1
        apartCnt += 1
        dfs(ny, nx)
        
for i in range(n) :
    for j in range(n) :
        if adjMatrix[i][j] == 0 : continue
        if visited[i][j] != 0 : continue
        danji += 1
        apartCnt += 1
        visited[i][j] = True
        dfs(i, j)
        ans.append(apartCnt)
        apartCnt = 0
        
ans.sort()
print(danji)
for i in ans :
    print(i)