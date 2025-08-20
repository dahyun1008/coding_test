import sys
from collections import defaultdict

input = sys.stdin.readline
n, m = map(int, input().split())
pair = (m//2) * n
data = defaultdict(int)
for _ in range(n):
    cur = list(map(int, input().split()))
    for i in range(m):
        data[cur[i]] += 1

for k in data.keys():
    pair -= data[k]//2

if pair <= 0:
    print("YES")
else:
    print("NO")