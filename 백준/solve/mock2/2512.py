import sys
import bisect

input = sys.stdin.readline
N = int(input())
data = list(map(int, input().split()))
M = int(input())

data.sort()
total = 0
for i in range(N):
    total += data[i]
if total <= M:
    print(data[-1])
else:
    result, high_price, high_amount = 0, data[-1], 0
    idx = len(data) - 1
    last = len(data) - 1
    # 
    while (idx >= 0):
        idx = bisect.bisect_left(data, high_price)
        high_amount = N - idx
        for i in range(last, idx-1, -1):
            total -= data[i]
        if total+high_amount * high_price <= M:
            break
        last = idx-1
        # high_price = data[last]
        high_price -= 1
    print(high_price)