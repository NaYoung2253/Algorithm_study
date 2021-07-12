import sys

N = int(sys.stdin.readline())
A = []

for i in range(N):
    A.append(list(map(int,sys.stdin.readline().split())))

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    merged_arr = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[r])
            r += 1

    merged_arr += left[l:]
    merged_arr += right[r:]

    return merged_arr

sort_arr = merge_sort(A)

for x in range(N):
    print(str(sort_arr[x][0]) + " " + str(sort_arr[x][1]))