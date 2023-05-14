import sys

st_l = list(input())
m = int(sys.stdin.readline())

st_r = []

for i in range(m) :
    mth = list(map(str, sys.stdin.readline().split()))
    
    if mth[0] == 'L' and st_l :
        st_r.append(st_l.pop())
    elif mth[0] == 'D' and st_r :
        st_l.append(st_r.pop())
    elif mth[0] == 'B' and st_l :
        st_l.pop()
    elif mth[0] == 'P' :
        st_l.append(mth[1])
        
print(''.join(st_l+list(reversed(st_r))))