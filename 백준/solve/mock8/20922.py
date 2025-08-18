import sys
from collections import defaultdict

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))
data_dict = defaultdict(int)

idx = 0
while idx < n and data_dict[data[idx]] < k:
    data_dict[data[idx]] += 1
    idx += 1

max_length, cur_length = idx, idx
s, e = 0, idx

while e < n:
    while data_dict[data[e]] >= k:
        cur_length -= 1
        data_dict[data[s]] -= 1
        s += 1
    while e < n and data_dict[data[e]] < k:
        cur_length += 1
        data_dict[data[e]] += 1
        e += 1
    max_length = max(max_length, cur_length)
print(max_length)