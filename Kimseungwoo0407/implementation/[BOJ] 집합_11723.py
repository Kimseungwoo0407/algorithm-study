import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    a = sys.stdin.readline().strip().split()

    if len(a) == 1:
        if a[0] == 'all':
            S = set(range(1, 21))
        else:
            S = set()

    else:
        x, y = a[0], a[1]
        y = int(y)

        if x == 'add':
            S.add(y)
        elif x == 'remove':
            S.discard(y)
        elif x == 'check':
            print(1 if y in S else 0)
        elif x == 'toggle':
            if y in S:
                S.discard(y)
            else:
                S.add(y)