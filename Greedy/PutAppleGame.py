n, m = map(int, input().split())
j = int(input())

start, end = 1, m
move = 0

for _ in range(j):
    apple = int(input())

    if apple > end:
        move += apple - end
        start += apple - end
        end = apple
    elif apple < start:
        move += start - apple
        end -= start - apple
        start = apple

print(move)