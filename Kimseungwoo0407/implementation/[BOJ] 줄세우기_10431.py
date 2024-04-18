T = int(input())

for test_case in range(T):
    students = list(map(int,input().split()))
    number, students = students[0], students[1:]
    result = [students[0]]
    cnt = 0

    for i in range(1,len(students)):
        for j in range(len(result)):
            if students[i] < result[j]:
                cnt += len(result)-j
                result.insert(j,students[i])
                break
        else:
            result.append(students[i])

    print(number,cnt)