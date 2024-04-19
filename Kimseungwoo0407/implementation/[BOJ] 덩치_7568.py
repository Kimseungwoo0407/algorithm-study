num = int(input())

result = []

for _ in range(num):
    a, b = map(int, input().split())
    result.append([a, b])

for i in range(len(result)):
    answer = 1
    for j in range(len(result)):
        if i != j and result[i][1] < result[j][1] and result[i][0] < result[j][0]:
            answer += 1
    print(answer, end=' ')