h, w = map(int, input().split())

ans = [[-1 for _ in range(w)] for _ in range(h)]

for i in range(h) :
    c = input()
    
    for j in range(w) :
        if c[j] == 'c' :
            ans[i][j] = 0
        else :
            if j > 0 and ans[i][j-1] >= 0 :
                ans[i][j] = ans[i][j-1] + 1
            else : ans[i][j] = -1
            
for i in range(h) :
    for j in range(w) :
        print(ans[i][j], end=' ')
    print()