H,W = map(int,input().split())

cloud = [ list(input()) for _ in range(H)]


visited = [ [-1] * W for _ in range(H)]

for i in range(len(cloud)):
    cnt = 0
    for j in range(W):
        if cloud[i][j] == 'c':
            visited[i][j] = 0
            cnt = 1
        elif cloud[i][j] == '.':
            if cnt > 0:
                visited[i][j] = cnt
                cnt +=1

for i in visited:
    for j in i:
        print(j,end=' ')
    print()