n, score, p = map(int, input().split())
answer = 0

if n == 0:
    answer = 1
else:
    board = sorted(list(map(int, input().split())), reverse=True)

    if n == p and board[-1] >= score:
        answer = -1

    else:
        answer = n + 1
        for i in range(n):
            if board[i] <= score:
                answer = i + 1
                break

print(answer)