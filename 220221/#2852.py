n = int(input())

time_list = []

win_times = [0, 0]
score_list = [0, 0]

for i in range(n):
    team, time = input().split()
    mint, sec = time.split(":")
    time_list.append((int(team), int(mint), int(sec)))

    if i == n - 1:
        time_list.append((int(team), 48, 00))

for i in range(n):
    name, mint, sec = time_list[i]
    win_times[name - 1] += 1

    n_name, n_min, n_sec = time_list[i + 1]

    if win_times[0] < win_times[1]:
        score_list[1] += n_min * 60 + n_sec - (mint * 60 + sec)
    elif win_times[0] > win_times[1]:
        score_list[0] += n_min * 60 + n_sec - (mint * 60 + sec)

for time in score_list:
    mint, sec = time // 60, time % 60
    print("{0}:{1}".format(str(mint).zfill(2), str(sec).zfill(2)))
