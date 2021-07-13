import sys

N = int(sys.stdin.readline())
A = []

for i in range(N):
    append_list = list(map(int,sys.stdin.readline().split()))
    A.append(list(reversed(append_list)))

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

sort_arr = quick_sort(A)

for x in range(N):
    print(str(sort_arr[x][1]) + " " + str(sort_arr[x][0]))