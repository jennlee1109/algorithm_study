while True:
    n = int(input())

    if n == 0:
        break

    words = []
    sorted_words = []

    for _ in range(n):
        word = input()
        words.append(word)
        sorted_words.append(word.lower())
        sorted_words.sort()

    for i in range(n):
        if words[i].lower() == sorted_words[0]:
            print(words[i])
            break