k = int(input())

cnt = 0
size = 0

i = 0
while k > size:
    size = 2 ** i
    i += 1

tmp = size
while k > 0:
    if k >= tmp:
        k -= tmp
    else:
        tmp //= 2
        cnt += 1

print(size, cnt)
