n = int(input())
cnt = 0

for _ in range(n) :
    st = []
    word = list(input())
    
    for i in word :
        if len(st) == 0 :
            st.append(i)
        else :
            if i == 'A' :
                if st[-1] == 'B' :
                    st.append(i)
                elif st[-1] == 'A' :
                    st.pop()
            elif i == 'B' :
                if st[-1] == 'A' :
                    st.append(i)
                elif st[-1] == 'B' :
                    st.pop()
                    
    if len(st) == 0 :
        cnt += 1
        
print(cnt)