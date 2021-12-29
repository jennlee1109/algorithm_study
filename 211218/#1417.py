def find_max():
    max_vote = 0
    max_candidate = 0

    for i in range(1, N):
        if max_vote < votes[i]:
            max_vote = votes[i]
            max_candidate = i

    return max_vote, max_candidate

N = int(input())

votes = [int(input()) for _ in range(N)]

if N == 1:
    print(0)
else:
    dasom_vote = votes[0]
    min_purchase = 0
    max_vote, max_candidate = find_max()

    while dasom_vote <= max_vote:
        dasom_vote += 1
        min_purchase += 1
        votes[max_candidate] -= 1
        max_vote, max_candidate = find_max()

    print(min_purchase)
