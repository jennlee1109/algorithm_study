n = int(input())

good_word = 0
for _ in range(n):
    word = input()

    stack = []

    for idx in range(len(word)):
        if len(stack) == 0:
            stack.append(word[idx])
        else:
            if stack[-1] == word[idx]:
                stack.pop()
            else:
                stack.append(word[idx])

    if len(stack) == 0:
        good_word += 1

print(good_word)