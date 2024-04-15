from collections import deque

F, S, G, U, D = map(int,input().split())

visited = [float('inf')] * (F+1)

def bfs(S):
    queue = deque()
    queue.append(S)
    visited[S] = 0
    while queue:
        s = queue.popleft()

        if s+U < F+1 and visited[s+U] > visited[s]+1:
            visited[s+U] = visited[s]+1
            queue.append(s+U)
        if s-D > 0 and visited[s-D] > visited[s]+1:
            visited[s-D] = visited[s]+1
            queue.append(s-D)
    return visited[G]

result = bfs(S)

if result == float('inf'):
    print('use the stairs')
else:
    print(result)
