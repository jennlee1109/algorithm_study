import heapq
import sys
n, k = map(int, sys.stdin.readline().split())

jewelry_list = []
bag_list = []
total = 0

for _ in range(n):
    weight, cost = map(int, sys.stdin.readline().split())
    jewelry_list.append((weight, cost))

jewelry_list.sort()
bag_list = [int(sys.stdin.readline()) for _ in range(k)]
bag_list.sort()

capable_heap = []

for i in range(k):
    while jewelry_list and bag_list[i] >= jewelry_list[0][0]:
        heapq.heappush(capable_heap, -jewelry_list[0][1])
        heapq.heappop(jewelry_list)

    if capable_heap:
        total += -heapq.heappop(capable_heap)
    elif not jewelry_list:
        break


print(total)
