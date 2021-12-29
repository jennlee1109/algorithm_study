u_board = list(map(int, input().split()))
s_board = list(map(int, input().split()))

win = False
u_sum = 0
s_sum = 0

for idx in range(9):
    u_sum += u_board[idx]

    if u_sum > s_sum:
        win = True

    s_sum += s_board[idx]

if win and u_sum < s_sum:
    print('Yes')
else:
    print('No')