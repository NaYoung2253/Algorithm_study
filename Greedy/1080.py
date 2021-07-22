import sys

def check(N, M):
    if (N < 3 or M < 3):
        return -1

N, M = map(int, sys.stdin.readline().split())
check(N, M)

A = []
B = []
cnt = 0

for i in range(N):
    arr = list(map(int, list(sys.stdin.readline().strip('\n'))))
    A.append(arr)

for i in range(N):
    arr = list(map(int, list(sys.stdin.readline().strip('\n'))))
    B.append(arr)

def swap(a, b):
    for i in range(a - 1, a + 2):
        for j in range(b - 1, b + 2):
            A[i][j] = 1 - A[i][j]

for i in range(1, N - 1):
    for j in range(1, M - 1):
        if (A[i - 1][j - 1] != B[i - 1][j - 1]):
            swap(i, j)
            cnt += 1

if (A == B):
    print(cnt)
else:
    print(-1)