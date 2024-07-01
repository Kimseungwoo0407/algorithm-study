import sys

input = sys.stdin.readline

S, C = map(int, input().split())
L = [int(input()) for _ in range(S)]

def make_pieces(length):
    count = 0
    for i in L:
        count += i // length
    return count >= C

start, end = 1, max(L)
result = 0

while start <= end:
    mid = (start + end) // 2
    if make_pieces(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

answer = sum(L) - result * C

print(answer)
