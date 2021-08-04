import sys

N = int(sys.stdin.readline())
voca = []
check = []

for i in range(N):
    info = []
    word = sys.stdin.readline().strip('\n')
    if word not in check:
        len_num = len(word)
        info.append(len_num)
        info.append(word)
        voca.append(info)
        check.append(word)

sort_arr = sorted(voca, key = lambda x : (x[0], x[1]))

for i in range(len(sort_arr)):
    print(sort_arr[i][1])