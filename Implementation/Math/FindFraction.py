x = int(input())

line = 0
end = 0

while x > end:
    line += 1
    end += line
    gap = end - x

    if line % 2 == 0:
        ja = line - gap
        mo = gap + 1
    else :
        ja = gap + 1
        mo = line - gap

print(ja, '/', mo, sep='')