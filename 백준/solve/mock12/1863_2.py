import sys

input = sys.stdin.readline
n = int(input())
count = 0
input_data = []
for _ in range(n):
    input_data.append(tuple(map(int, input().split())))
input_data.sort()
data = []

for i in range(n):
    (x, h) = input_data[i]
    while data and data[-1] > h:
        data.pop()
    if not data or data[-1] < h:
        if h != 0:
            count += 1
        data.append(h)
    else:
        continue

print(count)