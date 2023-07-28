# https://www.acmicpc.net/problem/20413

n = int(input())
s, g, p, d = map(int, input().split())
grade = list(map(str, input()))

total = 0
prev = 0

for i in range(n):
    if grade[i] == 'B':
        total += s - 1 - prev
        prev = s - 1 - prev
    elif grade[i] == 'S':
        total += g - 1 - prev
        prev = g - 1 - prev
    elif grade[i] == 'G':
        total += p - 1 - prev
        prev = p - 1 - prev
    elif grade[i] == 'P':
        total += d - 1 - prev
        prev = d - 1 - prev
    elif grade[i] == 'D':
        total += d
        prev = d

print(total)
