import heapq

n = int(input())

heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))
result = 0

while len(heap) > 1:
    total = heapq.heappop(heap) + heapq.heappop(heap)
    # print(total)
    result += total
    heapq.heappush(heap, total)
    # print(heap)

print(result)