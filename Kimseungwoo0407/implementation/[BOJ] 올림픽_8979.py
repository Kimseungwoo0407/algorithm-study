N, M = map(int,input().split())

country = []

for _ in range(N):
    country.append(list(map(int,input().split())))

country.sort(key=lambda x: (x[1],x[2],x[3]),reverse=True)

result = [(country[0][0],1)]
rank = 1
same_rank = 1

for i in range(1,len(country)):
    if country[i][1:] == country[i-1][1:]:
        result.append((country[i][0],rank))
        same_rank += 1
    else:
        rank += same_rank
        result.append((country[i][0],rank))
        same_rank = 1

for i in result:
    if i[0] == M:
        print(i[1])