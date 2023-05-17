a, b, c = list(map(int, input().split()))

time = [0 for _ in range(101)]
total = 0

for _ in range(3) :
    arr, lft = list(map(int, input().split()))
    
    for i in range(arr, lft) :
        time[i] += 1

for i in time :
    if i != 0 :
        if i == 1 : total += a
        elif i == 2 : total += 2 * b
        elif i == 3 : total += 3 * c
        
print(total)