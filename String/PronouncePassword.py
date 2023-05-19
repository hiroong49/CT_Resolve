vowels = ['a', 'e', 'i', 'o', 'u']

while True :
    flag = 0
    vowel = 0
    v_cnt = 0
    c_cnt = 0

    s = input()
    
    if s == 'end' :
        break
    
    for i in range(len(s)) :
        if i > 0 :
            if s[i] == s[i-1] :
                if s[i] != 'e' and s[i] != 'o' :
                    flag = -1
                    break
                    
        if s[i] in vowels :
            vowel = 1 
            v_cnt += 1
            c_cnt = 0
            if v_cnt >= 3 :
                flag = -1
                break
            
        else :
            c_cnt += 1
            v_cnt = 0
            if c_cnt >=3 :
                flag = -1
                break

        
    if flag == 0 and vowel == 1 :
        print('<', s, '> is acceptable.', sep='')
    else :
        print('<', s, '> is not acceptable.', sep='')
            
