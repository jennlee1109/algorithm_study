word = input()

size = len(word)

min_val = 'z' * 50

for i in range(size-2):
    first = word[:i+1]

    for j in range(i+1, size-1):
        second = word[i+1:j+1]
        third = word[j+1:]

        tmp = first[::-1] + second[::-1] + third[::-1]
        min_val = min(min_val, tmp)

print(min_val)