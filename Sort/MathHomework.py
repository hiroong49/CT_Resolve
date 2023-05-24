n = int(input())

ans = []

for _ in range(n):
    s = input()
    num = ''
    
    for i in s:
        if i.isdigit():
            num += i
        else:
            if num:
                ans.append(int(num))
                num = ''
            else:
                num = ''

    if num:
        ans.append(int(num))
    
ans.sort()
for i in ans:
    print(i)