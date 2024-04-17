A,B,C = map(int,input().split())

time = [0]*101
cost = 0

for test_case in range(3):
    a,b = map(int,input().split())
    for i in range(a+1,b+1):
        time[i] += 1

for i in time:
    if i == 1:
        cost += A
    elif i == 2:
        cost += B*i
    elif i == 3:
        cost += C*i

print(cost)