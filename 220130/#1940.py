n = int(input())
m = int(input())

materials = list(map(int, input().split()))
materials.sort()

cnt = 0
i, j = 0, n-1

while i < j:
    if materials[i] + materials[j] == m:
        cnt += 1
        i += 1
        j -= 1
    elif materials[i] + materials[j] < m:
        i += 1
    else:
        j -= 1

print(cnt)