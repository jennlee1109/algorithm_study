answer = []
def b_notation(b, num):
    global answer

    while num >= b:
        answer.append(num % b)
        num //= b

    answer.append(num)


a, b = map(int, input().split())
m = int(input())

a_notation = list(map(int, input().split()))

result = 0

i = 0
for num in a_notation[::-1]:
    result += a ** i * num
    i += 1

b_notation(b, result)

for num in answer[::-1]:
    print(num, end=" ")