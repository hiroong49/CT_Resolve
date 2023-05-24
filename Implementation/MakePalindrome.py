s = input()
s = sorted(s)

arr = [0 for _ in range(26)]
odd = 0
str_odd = ''
alp = ''

for i in s:
    arr[ord(i)-65] += 1
    
for i in range(26):
    if arr[i] % 2 == 1:
        odd += 1
        str_odd += chr(i+65)
    alp += chr(i+65) * (arr[i] // 2)

if odd > 1 :
    print("I'm Sorry Hansoo")
else:
    print(alp + str_odd + alp[::-1])
    