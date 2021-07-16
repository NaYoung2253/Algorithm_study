import sys
import re

N = int(sys.stdin.readline())
A = []

for i in range(N):
    info = []
    number = sys.stdin.readline().strip('\n')
    len_num = len(number)
    sum_num = sum(list(map(int, (re.sub(r'[^0-9]', '', number)))))
    info.append(len_num)
    info.append(sum_num)
    info.append(number)
    A.append(info)

sort_arr = sorted(A, key = lambda x : (x[0], x[1], x[2]))

for x in range(N):
    print(sort_arr[x][2])