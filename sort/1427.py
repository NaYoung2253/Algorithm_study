import sys

N = int(sys.stdin.readline())
number = []

while (N != 0):
    number.append(N % 10)
    N = N // 10

def count_sort(arr):
    count = [0] * 11
    result = ''

    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in reversed(range(len(count))):
        if count[i] != 0:
            for j in range(count[i]):
                result += str(i)

    print(result)

count_sort(number)