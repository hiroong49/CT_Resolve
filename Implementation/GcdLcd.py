n, m = map(int, input().split())

# 최대공약수
def gcd(a, b) :
    # b와 r(a를 b로 나눈 나머지)의 최대공약수와 같다 (a>b) 
    while b > 0 :
        a, b = b, (a % b)
    return a
    
# 최소공배수
def lcd(a, b) :
    # a와 b를 곱한 값을 a, b의 최대공약수로 나눈다
    return a * b // gcd(a, b)
    
print(gcd(n, m))
print(lcd(n, m))