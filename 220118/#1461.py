n, m = map(int, input().split())

books = list(map(int, input().split()))
books.sort()

m_books = []
p_books = []
cnt = 0

for i in range(n):
    if books[i] < 0:
        m_books.append(books[i])
    else:
        p_books.append(books[i])

result = []

i = 0
while i < len(m_books):
    result.append(m_books[i:i+m])
    i += m

# j = len(p_books)
while p_books:
    tmp = []
    for i in range(m):
        if p_books:
            tmp.append(p_books.pop())
        else:
            break
    tmp.sort()
    result.append(tmp)

result.sort()
# print(result)
if abs(result[0][0]) < result[-1][-1]:
    for i in range(len(result)):
        if result[i][0] < 0:
            if i == len(result) - 1:
                cnt += -result[i][-1]
            else:
                cnt += -result[i][0] * 2
        else:
            if i == len(result) - 1:
                cnt += result[i][-1]
            else:
                cnt += result[i][-1] * 2


else:
    for i in range(len(result)):
        if result[i][0] < 0:
            if i == 0:
                cnt += -result[0][0]
            else:
                cnt += -result[i][0] * 2
        else:
            if i == 0:
                cnt += result[0][0]
            else:
                cnt += result[i][-1] * 2

print(cnt)