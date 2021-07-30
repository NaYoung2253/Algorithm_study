import sys

N = int(sys.stdin.readline())
tips = []

for i in range(N):
    tips.append(int(sys.stdin.readline().strip()))

sort_tip = sorted(tips, reverse=True)

sum = 0
for i in range(N):
    tip = sort_tip[i] - i
    if tip < 0:
        continue
    
    sum += tip

print(sum)