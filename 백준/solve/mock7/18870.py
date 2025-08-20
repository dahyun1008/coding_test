import sys, bisect

input = sys.stdin.readline
n = int(input())
input_data = list(map(int, input().split()))

data = []
for i in range(n):
    data.append((input_data[i], i))

data.sort()

count = []
temp = []
for i in range(n):
    idx = bisect.bisect_left(temp, data[i][0])
    count.append((idx, data[i][1]))
    if idx != len(temp) and temp[idx] == data[i][0]:
        continue
    temp.append(data[i][0])

result = [0] * n
for i in range(n):
    result[count[i][1]] = count[i][0]

print(' '.join(str(i) for i in result))