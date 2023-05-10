t = int(input())

for _ in range(t) :
    n = int(input())
    
    score = []

    for _ in range(2) :
        score.append(list(map(int, input().split())))
        
    for i in range(1, n) :
        if i == 1 :
            score[0][i] += score[1][i-1]
            score[1][i] += score[0][i-1]
        else :
            score[0][i] += max(score[1][i-1], score[1][i-2])
            score[1][i] += max(score[0][i-1], score[0][i-2])
    print(max(score[0][n-1], score[1][n-1]))