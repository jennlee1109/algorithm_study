cnt = 0
def good_section(start, end):
    global cnt
    for i in range(start, n + 1):
        for j in range(i + 1, end):
            if i <= n <= j:
                cnt += 1

L = int(input())
S = list(map(int, input().split()))
n = int(input())

S.append(n)
S.sort()

idx = 0

for i in range(len(S)):
    if S[i] == n:
        idx = i
        break

if idx == 0:
    start, end = 1, S[idx+1]
    good_section(start, end)
else:
    start, end = S[idx-1], S[idx+1]
    good_section(start+1, end)

print(cnt)