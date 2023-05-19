n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

ans = 0
ans += n

for i in a :
    i -= b
    if i > 0 :
        if i % c == 0 :
            ans += i // c
        else : ans += i // c + 1

print(ans)