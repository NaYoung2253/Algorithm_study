import sys

num = list(sys.stdin.readline().strip())
sum = ''

if '0' not in num:
    print(-1)
else:
    sort_num = sorted(num, reverse=True)

    for i in range(len(sort_num)):
        sum += sort_num[i]
    
    if int(sum) % 3 != 0:
        print(-1)
    else:
        print(sum)