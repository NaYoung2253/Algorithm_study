import sys

N, M, K = map(int, sys.stdin.readline().split())
team = 0

while N >= 2 and M >= 1 and N + M - 3 >= K:
    N -= 2
    M -= 1
    team += 1

print(team)