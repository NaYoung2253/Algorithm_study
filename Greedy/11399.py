import sys

N = int(sys.stdin.readline())
array = list(map(int, input().split()))
result = 0

sort_arr = sorted(array)

for i in range(N):
    result += sort_arr[i] * (N - i)

print(result)