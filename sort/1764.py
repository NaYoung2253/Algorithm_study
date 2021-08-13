import sys

N, M = map(int, sys.stdin.readline().split())
unheard = set()
unseen = set()

for i in range(N):
    unheard.add(sys.stdin.readline().strip('\n'))

for j in range(M):
    unseen.add(sys.stdin.readline().strip('\n'))

intersect = sorted(list(unheard & unseen))

cnt = len(intersect)
print(cnt)
for i in range(cnt):
    print(intersect[i])