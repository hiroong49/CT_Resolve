# https://www.acmicpc.net/problem/5568

from itertools import permutations

card = []
st = []

n = int(input())
k = int(input())

for _ in range(n):
    card.append(input())

for i in permutations(card, k):
    st.append(''.join(i))

print(len(set(st)))