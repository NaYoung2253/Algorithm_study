import sys

N = int(sys.stdin.readline())
A = []

for i in range(N):
    append_list = sys.stdin.readline().split()
    name = [append_list[0]]
    score = list(map(int, append_list[1:]))
    A.append(score + name)

sort_arr = sorted(A, key = lambda x : (-x[0], x[1], -x[2], x[3]))

for x in range(N):
    print(sort_arr[x][3])