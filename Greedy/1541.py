import sys

str = sys.stdin.readline().split('-')
num = []

for i in str:
    plus = 0
    plus_num = i.split('+')
    for j in plus_num:
        plus += int(j)
    num.append(plus)

result = num[0]

for i in range(1, len(num)):
    result -= num[i]

print(result)