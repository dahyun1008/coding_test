import sys
from collections import defaultdict

input = sys.stdin.readline
n, m, t, k = map(int, input().split())
cur = list(map(int, input().split()))
first = 0
data = defaultdict(int)
for _ in range(k):
    r, c1, c2, color = map(int, input().split())
    r -= 2
    for i in range(m):
        data[cur[i]] += r - first + 1
    first = r + 1
    for i in range(c1-1, c2):
        cur[i] = color
    print(cur)

print(' '.join(str(data[i]) for i in range(1, t+1)))