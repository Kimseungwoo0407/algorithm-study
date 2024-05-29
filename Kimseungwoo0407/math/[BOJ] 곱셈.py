A,B,C = map(int,input().split())

def problem(A,B):
    if B == 1:
        return A%C
    else:
        temp = problem(A, B // 2)
        if B % 2 == 0:
            return temp * temp % C
        else:
            return temp * temp * A % C

print(problem(A,B))