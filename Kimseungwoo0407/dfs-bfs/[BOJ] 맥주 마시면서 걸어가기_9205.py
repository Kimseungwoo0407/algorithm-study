from collections import deque
t = int(input())

def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        if abs(x-festival_x) + abs(y-festival_y) <= 1000:
            print('happy')
            return

        for i in range(market): # 편의점 확인
            if not visited[i]:
                new_x,new_y = markets[i]
                if abs(x-new_x) + abs(y-new_y) <= 1000:
                    visited[i] = 1
                    q.append((new_x,new_y))
    print('sad')
    return

for test_case in range(t):
    market = int(input())
    house_x, house_y = map(int, input().split())
    markets = []
    for i in range(market):
        x,y = map(int,input().split())
        markets.append((x,y))
    festival_x,festival_y = map(int,input().split())
    visited = [0] * (market+1)
    bfs(house_x,house_y)

