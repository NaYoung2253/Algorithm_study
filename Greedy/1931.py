import sys

N = int(sys.stdin.readline())
A = []

for i in range(N):
    room_info = list(map(int, sys.stdin.readline().split()))
    A.append(room_info)

sort_arr = sorted(A, key = lambda x : (x[1], x[0]))

check = 0
cnt = 0
for j in range(len(sort_arr)):
    if (check <= sort_arr[j][0]):
        check = sort_arr[j][1]
        cnt += 1

print(cnt)