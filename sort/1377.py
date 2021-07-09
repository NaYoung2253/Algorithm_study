import sys

N = int(sys.stdin.readline())
A = []

for i in range(N):
    A.append((int(sys.stdin.readline()), i))

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

sort_arr = sorted(A)

idx = []
for x in range(N):
    idx.append(sort_arr[x][1] - x)

count = max(idx)
print(count + 1)
