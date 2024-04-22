N,New_score,P = map(int,input().split())

if N == 0:
    print(1)
else:
    score = list(map(int,input().split()))
    if N == P and score[-1] >= New_score:
        print(-1)
    else:
        rank = N + 1
        for i in range(N):
            if score[i] <= New_score:
                rank = i + 1
                break
        print(rank)