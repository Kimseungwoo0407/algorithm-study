nums = int(input())
switch = list(map(int,input().split()))
students = int(input())

for _ in range(students):
    a,b = map(int,input().split())
    b = b - 1

    if a == 1:
        for i in range(b,nums,b+1):
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1
    elif a == 2:
        left = right = b
        while left > 0 and right < nums -1 and  switch[left-1] == switch[right+1]:
            left -= 1
            right +=1
        for i in range(left,right+1):
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1

cnt = 0
for i in switch:
    cnt += 1
    if cnt > 20:
        print()
        cnt = 1
    print(i, end=' ')
