n = int(input())

first = []
ans = []

for _ in range(n) :
    name = list(map(str, input()))
    first.append(name[0])
    
set_first = set(first)

for i in set_first :
    if first.count(i) >= 5 :
        ans.append(i)

ans.sort()

if len(ans) > 0 :
    print(''.join(ans))
else :
    print('PREDAJA')