n, k = map(int, input().split())

arr = [i for i in range(1, n+1)]
index = 0
st = []

for i in range(n) :
    index += k - 1
    if index >= len(arr) :
        index = index % len(arr)
        
    st.append(str(arr[index]))
    arr.pop(index)

print('<', ', '.join(st), '>', sep='')