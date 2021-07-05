import sys

N = int(sys.stdin.readline())
array = []

for i in range(N):
    x = int(sys.stdin.readline())
    if x not in array:
        array.append(x)

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
    
#     print(array[0])
#     pivot = array[0]
#     tail = array[1:]

#     left = [x for x in tail if x <= pivot]
#     right = [x for x in tail if x > pivot]

#     return quick_sort(left) + [pivot] + quick_sort(right)

# array = quick_sort(array)

sort_array = sorted(array)

for i in range(len(sort_array)):
    print(sort_array[i])