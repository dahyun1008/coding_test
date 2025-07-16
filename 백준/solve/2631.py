import sys
import bisect

input = sys.stdin.readline
n = int(input())
children = []
for _ in range(n):
    children.append(int(input()))

part_arr = []

for child in children:
    idx = bisect.bisect_left(part_arr, child)
    if len(part_arr) <= idx:
        part_arr.append(child)
    else:
        part_arr[idx] = child

print(n-len(part_arr))