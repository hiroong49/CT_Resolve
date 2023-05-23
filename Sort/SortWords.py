n = int(input())

words = []
for _ in range(n):
    words.append(input())

set_words = set(words)
set_words = sorted(set_words)
set_words = sorted(set_words, key=len)

print(set_words)

