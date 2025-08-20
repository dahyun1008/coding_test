import sys

input = sys.stdin.readline
n = int(input())

max_h = 0
data = []
for _ in range(n):
    l, h = map(int, input().split())
    max_h = max(max_h, h)
    data.append((l, h))

data.sort()
result = 0
# 최고 높이 이전 처리
idx = 0
while data[idx][1] < max_h:
    next = idx+1
    while data[next][1] <= data[idx][1]:
        next += 1
    result += data[idx][1] * (data[next][0]-data[idx][0])
    idx = next

# idx는 최고 높이 시작점
next = idx+1
while next < len(data) and data[next][1] == max_h:
    next += 1
result += max_h * (data[next-1][0]+1-data[idx][0])

# 최고 높이 이후(next: 최고 높이 이후 첫 번째 기둥)
max_end = next - 1
idx = len(data)-1
while idx > max_end:
    next = idx-1
    while next > max_end and data[next][1] <= data[idx][1]:
        next -= 1
    result += data[idx][1] * (data[idx][0]-data[next][0])
    idx = next

print(result)