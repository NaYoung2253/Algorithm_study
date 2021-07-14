import sys

N = int(sys.stdin.readline())

def count_sort(N):
    count = {}

    for i in range(N):
        input = int(sys.stdin.readline())
        if input not in count:
            count[input] = 1
        else:
            count[input] += 1

    count = list(zip(count.values(), count.keys()))
    sort_count = sorted(count, key = lambda x : (-x[0], x[1]))

    print(sort_count[0][1])

count_sort(N)