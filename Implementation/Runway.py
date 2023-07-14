

n, l = map(int, input().split())
runway = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

def way(pos):
    for i in range(1, n):
        if abs(pos[i] - pos[i-1]) > 1:
            return False
        if pos[i] < pos[i-1]:
            for j in range(l):
                if i + j >= n or used[i+j] or pos[i] != pos[i+j]:
                    return False
                if pos[i] == pos[i+j]:
                    used[i+j] = True
        elif pos[i] > pos[i-1]:
            for j in range(l):
                if i - j - 1 < 0 or used[i-j-1] or pos[i-1] != pos[i-j-1]:
                    return False
                if pos[i-1] == pos[i-j-1]:
                    used[i-j-1] = True
    return True

# 가로
for i in range(n):
    used = [False for _ in range(n)]
    if way(runway[i]):
        cnt += 1

# 세로
for i in range(n):
    used = [False for _ in range(n)]
    if way([runway[j][i] for j in range(n)]):
        cnt += 1

print(cnt)

