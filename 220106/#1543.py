words = input()
target = input()

idx = 0
cnt = 0

while idx < len(words):
    if words[idx:idx+len(target)] == target:
        idx += len(target)
        cnt += 1
    else:
        idx += 1

print(cnt)