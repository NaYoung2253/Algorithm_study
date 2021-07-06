import sys

N = int(sys.stdin.readline())
array = []

for i in range(N):
    array.append(int(sys.stdin.readline()))

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    print(left)
    print(right)

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

sort_array = merge_sort(array)

for i in range(len(sort_array)):
    print(sort_array[i])