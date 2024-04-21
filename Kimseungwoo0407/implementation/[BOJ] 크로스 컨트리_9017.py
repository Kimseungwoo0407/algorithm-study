T = int(input())

for test_case in range(T):
    iteration = int(input())
    people = list(map(int,input().split()))
    team = set(people)

    real_team = []
    for i in team:
        if people.count(i) == 6:
            real_team.append(i)

    scores = [ [] for _ in range(max(people)+1)]
    score = 0
    for i in people:
        if i in real_team:
            score += 1
            scores[i].append(score)
    result = []
    for i in range(len(scores)):
        if i in real_team:
            result.append((sum(scores[i][:4]),scores[i][4],i))

    result.sort(key= lambda x : (x[0],x[1]))

    print(result[0][2])