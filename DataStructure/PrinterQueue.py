from collections import deque

t = int(input())

for _ in range(t):
    cnt = 0

    n, m = map(int, input().split())
    que = deque(list(map(int, input().split())))

    while m != -1:
        if que[0] == max(que):
            que.popleft()
            cnt += 1
            m -= 1
        else:
            que.append(que.popleft())

            if m == 0:
                m = len(que) - 1
            else:
                m -= 1

    print(cnt)
