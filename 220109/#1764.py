import sys
n, m = map(int, input().split())

people_dic = dict()
result = []

for i in range(n+m):
    name = input()
    if name in people_dic.keys():
        people_dic[name] += 1
    else:
        people_dic[name] = 1

for key in people_dic.keys():
    if people_dic[key] >= 2:
        result.append(key)

result.sort()
print(len(result))

for name in result:
    print(name)