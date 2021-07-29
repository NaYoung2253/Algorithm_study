import sys

N = int(sys.stdin.readline())
coins = [500, 100, 50, 10, 5, 1]

change = 1000 - N
cnt = 0

for coin in coins:
    cnt += change // coin
    change = change % coin

print(cnt)