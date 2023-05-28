n = int(input())

flag = 0
one, two = 0, 0

for _ in range(n):
    team, time = map(str, input().split())
    min, sec = map(int, time.split(':'))

    goal = 48*60 - (min*60 + sec)

    if team == '1':
        if flag == 0:
            one += goal
        flag += 1

        if flag == 0 and two > 0:
            two = two - goal

    else:
        if flag == 0:
            two += goal
        flag -= 1

        if flag == 0 and one > 0:
            one = one - goal

print('{:0>2}:{:0>2}'.format(one//60, one%60))
print('{:0>2}:{:0>2}'.format(two//60, two%60))