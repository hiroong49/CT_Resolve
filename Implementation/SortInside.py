# https://www.acmicpc.net/problem/1427

n = list(map(str, input()))

n.sort(reverse=True)
print(''.join(n))