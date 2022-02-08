import math
import sys
n = int(sys.stdin.readline())
fence_list = []
distance = []

for i in range(n):
    fence_list.append(int(sys.stdin.readline()))
    if i > 0:
        distance.append(fence_list[i] - fence_list[i - 1])

gcd_num = distance[0]

for i in range(1, len(distance)):
    gcd_num = math.gcd(gcd_num, distance[i])

cnt = 0

for i in range(len(distance)):
    cnt += (distance[i] // gcd_num) - 1

print(cnt)
