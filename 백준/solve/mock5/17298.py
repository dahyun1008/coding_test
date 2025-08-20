import sys

input = sys.stdin.readline
n = int(input())

data = list(map(int, input().split()))
result = [(0, 0)] * len(data)
for i in range(len(data)-1, -1, -1):
    if i == len(data)-1:
        result[i] = (-1, -1)
        continue
    if data[i] < data[i+1]:
        result[i] = (i+1, data[i+1]) # 위치 인덱스, 오큰수의 값
    else: # 오른쪽 수가 같거나 작은 경우
        next = result[i+1][0]
        while data[i] >= data[next]:
            next = result[next][0]
            if next == -1:
                break
        if next == -1:
            result[i] = (-1, -1)
        else:
            result[i] = (next, data[next])

print(' '.join(str(result[i][1]) for i in range(len(result))))