import sys
from collections import defaultdict
input = sys.stdin.readline
n, m = map(int, input().split())
book = defaultdict(int)

for _ in range(n):
    data = input().strip()
    if len(data) < m:
        continue
    book[data]+=1

words = []
for k in book.keys():
    words.append((-1*book[k], -1*len(k), k))

words.sort()
for w in words:
    print(w[2])