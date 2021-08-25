import sys

N, K = map(int, sys.stdin.readline().split())
nums = [[0] * 201 for i in range(201)]

for i in range(201):
    nums[i][1] = 1

for i in range(1, 201):
    for j in range(201):
        for l in range(j + 1):
            nums[j][i] += nums[l][i - 1]

print(nums[N][K] % 1000000000)