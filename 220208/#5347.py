def gcd(a, b):
    if a < b:
        a, b = b, a

    if b == 0:
        return a
    else:
        return gcd(b, a % b)


n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    gcd_num = gcd(a, b)

    print((a * b) // gcd_num)
