m = int(input())

ball = 1

for i in range(m):
    x, y = map(int, input().split())

    if ball == x :
        ball = y
    elif ball == y :
        ball = x
    
print(ball)