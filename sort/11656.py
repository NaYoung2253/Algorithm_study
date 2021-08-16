import sys

S = sys.stdin.readline().strip('\n')
suffixes = []

for i in range(len(S)) :
    suffixes.append(S[i:])

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

sort_suf = quick_sort(suffixes)

for i in range(len(sort_suf)):
    print(sort_suf[i])