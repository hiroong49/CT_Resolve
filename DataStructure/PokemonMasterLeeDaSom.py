import sys

n, m = map(int, sys.stdin.readline().split())
pokemon = {}

for i in range(1, n+1) :
    mon = sys.stdin.readline().rstrip()
    pokemon[i] = mon
    pokemon[mon] = i
    
for i in range(m) :
    q = sys.stdin.readline().rstrip()
    
    if q.isdigit() :
        print(pokemon[int(q)])
        
    else :
        print(pokemon[q])
    