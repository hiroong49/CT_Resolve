n = int(input())
a, b = input().split('*')

for _ in range(n) :
    file = input()
    
    if len(a) + len(b) > len(file) :
        print('NE')
    else :
        if file[:len(a)] == a and file[-len(b)::] == b :
            print('DA')
        else : 
            print('NE')