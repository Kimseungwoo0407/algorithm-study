from collections import deque

N = int(input())
li=[]
for i in range(1,N+1):
    li.append(i)

queue = deque(li)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())


print(queue[0])