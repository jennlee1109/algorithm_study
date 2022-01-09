t = int(input())

for _ in range(t):
    n = int(input())

    scores = []

    for _ in range(n):
        d_score, i_score = map(int, input().split())
        scores.append((d_score, i_score))

    scores.sort()
    cnt = 1

    prev_d, prev_i = scores[0][0], scores[0][1]

    for i in range(1, n):

        if prev_d <= scores[i][0]:
            if prev_i > scores[i][1]:
                cnt += 1
                prev_d, prev_i = scores[i][0], scores[i][1]
        else:
            cnt += 1
            prev_d, prev_i = scores[i][0], scores[i][1]

    print(cnt)

