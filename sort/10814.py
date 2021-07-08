import sys

N = int(sys.stdin.readline())

def count_sort(N):
    count = [0] * 201
    name = [''] * 201

    for i in range(N):
        input = sys.stdin.readline().split()
        count[int(input[0])] += 1
        name[int(input[0])] += (input[1] + '/')

    for i in range(len(count)):
        if count[i] != 0:
            names = name[i].split('/')
            for j in range(count[i]):
                print(str(i) + ' ' + names[j])

count_sort(N)