def isPanlindrome(word1, word2):
    result = word1 + word2
    return result == result[::-1]

def main(words, size):
    for i in range(size - 1):
        for j in range(i + 1, size):
            if isPanlindrome(words[i], words[j]):
                print(words[i] + words[j])
                return
            if isPanlindrome(words[j], words[i]):
                print(words[j] + words[i])
                return

    print(0)


n = int(input())

for _ in range(n):
    size = int(input())
    words = [input() for _ in range(size)]

    main(words, size)
