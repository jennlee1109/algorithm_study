n = int(input())

for _ in range(n):
    msg = input()

    alphabet = dict()

    idx = 0
    fake = False

    while idx < len(msg):
        word = msg[idx]
        if word not in alphabet.keys():
            alphabet[word] = 1
        else:
            alphabet[word] += 1

        if alphabet[word] % 3 == 0:
            if idx == len(msg) - 1 or word != msg[idx+1]:
                fake = True
                break
            else:
                idx += 1

        idx += 1

    if fake:
        print('FAKE')
    else:
        print('OK')

