import sys

N, K = map(int, sys.stdin.readline().split())
array = []

for i in range(N):
    array.append(int(sys.stdin.readline()))

cnt = 0

for i in range(N - 1, -1, -1):
    if (array[i] > K):
        continue
    elif (K == 0):
        break
    cnt += K // array[i]
    K %= array[i]

print(cnt)
