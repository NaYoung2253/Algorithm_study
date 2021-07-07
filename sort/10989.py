import sys

N = int(sys.stdin.readline())

def count_sort(N):
    count = [0] * 10001

    for i in range(N):
        count[int(sys.stdin.readline())] += 1

    for i in range(len(count)):
        if count[i] != 0:
            for j in range(count[i]):
                print(i)

count_sort(N)