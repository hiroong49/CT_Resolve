a, b, v = map(int, input().split())

climb = (v - b) // (a - b)

if (v - b) % (a - b) == 0:
    print(climb)
else :
    print(climb + 1)
