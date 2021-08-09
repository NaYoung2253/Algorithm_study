import sys 
from collections import Counter

N = int(sys.stdin.readline())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))
    
def mean(nums):
    return round(sum(nums)/len(nums))

def middle(nums):
    sort_num = sorted(nums)
    mid = sort_num[len(nums)//2]
    
    return mid

def mode(nums):
    sort_num = sorted(nums)
    mode_count = Counter(sort_num)
    most_mode = mode_count.most_common()    
    
    if len(nums) > 1: 
        if most_mode[0][1] == most_mode[1][1]:
            return most_mode[1][0]
        else : 
            return most_mode[0][0]
    else : 
        return most_mode[0][0]
        
def range(nums):
    return max(nums) - min(nums)

print(mean(nums))
print(middle(nums))
print(mode(nums))
print(range(nums))