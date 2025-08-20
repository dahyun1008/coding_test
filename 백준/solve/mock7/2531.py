import sys
from collections import deque
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

max_count = 0
cur = deque()
for i in range(k):
    cur.append(data[i])
    max_count = len(set(cur) | {c})
for i in range(1, n):
    cur.popleft()
    cur.append(data[(i+k-1)%n])
    max_count = max(max_count, len(set(cur) | {c}))

print(max_count)