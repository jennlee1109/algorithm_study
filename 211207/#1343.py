board = input()

answer = ''
board_list = []
tmp = ''

if len(board) % 2 != 0:
    print('-1')

else:
    for b in board:
        if b == 'X':
            tmp += b
        elif b == '.':
            board_list.append(tmp)
            board_list.append('.')
            tmp = ''
        else:
            answer = -1
            break

    if answer == -1 or board == '':
        print('-1')
    else:
        if tmp != '':
            board_list.append(tmp)

        board_list = ' '.join(board_list).split()

        result = []
        for board in board_list:
            if board == '.':
                result.append('.')
                continue
            board_len = len(board)

            tmp = ''
            while board_len >= 4:
                tmp += (board_len // 4) * 'AAAA'
                board_len %= 4

            while board_len % 2 == 0 and board_len >= 2:
                tmp += (board_len // 2) * 'BB'
                board_len %= 2

            result.append(tmp)

        for r in result:
            if r == '':
                answer = '-1'
                break
            else:
                answer += r

        print(answer)
