n = int(input())
bee = 1
cnt = 1

while n > bee:
    bee += cnt * 6
    cnt += 1
print(cnt)