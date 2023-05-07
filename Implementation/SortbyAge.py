import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    lst.append([int(age), i, name])
    
lst.sort()

for i in range(n):
    print(lst[i][0], lst[i][2])