import sys
import copy

input = sys.stdin.readline
_ = input()
data = list(map(int, input().split()))
left = copy.deepcopy(data)
right = copy.deepcopy(data)

left_max = 0
for i in range(len(data)):
    if left_max > left[i]:
        left[i] = left_max
    else:
        left_max = left[i]

right_max = 0
for i in range(len(data)-1, -1, -1):
    if right_max >right[i]:
        right[i] = right_max
    else:
        right_max = right[i]

result = 0
for i in range(len(data)):
    min_h = min(left[i], right[i])
    result += min_h - data[i]
print(result)