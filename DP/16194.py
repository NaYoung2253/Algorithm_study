import sys 

N = int(sys.stdin.readline())
P = [0] + list(map(int, sys.stdin.readline().split()))
money = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(1, i + 1):
        if money[i] != 0:
            money[i] = min(money[i], P[j] + money[i - j])
        else:
            money[i] = P[j] + money[i - j]
print(money[N])