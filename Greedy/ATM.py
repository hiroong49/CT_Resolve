n = int(input())
p = list(map(int, input().split()))

waiting = 0
total = []

p.sort()
for i in p:
    waiting += i
    total.append(waiting)

print(sum(total))
