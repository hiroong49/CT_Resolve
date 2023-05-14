while True :
    try :
        s = list(input())
        
        up, low, digit = 0, 0, 0
        
        for i in s :
            if i.isupper() :
                up += 1
            if i.islower() :
                low += 1
            if i.isdigit() :
                digit += 1
                
        print(low, up, digit, s.count(' '))
        
    except EOFError :
        break