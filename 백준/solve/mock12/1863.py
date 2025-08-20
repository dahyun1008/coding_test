import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
data = []
for _ in range(n):
    data.append(tuple(map(int, input().split())))
visited = defaultdict(int)
data.sort()
count = 0
for i in range(n):
    if visited[data[i][1]]:
        pass
    elif not visited[data[i][1]] and data[i][1] != 0:
        count += 1
        visited[data[i][1]] = 1
    for k in visited.keys():
        if k > data[i][1]:
            visited[k] = 0

print(count)