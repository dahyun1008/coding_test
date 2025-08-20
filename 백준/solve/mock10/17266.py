import sys

input = sys.stdin.readline
n = int(input()) # 길이가 n이면 지점은 n+1 존재
m = int(input())
data = list(map(int, input().split()))

def can(height):
    # data: 가로등을 놓을 수 있는 위치 인덱스가 들어 있음
    light = [0] * n
    for i in range(m):
        for j in range(data[i]-1, data[i]-height-1, -1):
            if 0 <= j < n:
                if light[j]:
                    break
                light[j] = 1
        for j in range(data[i], data[i]+height):
            if 0 <= j < n:
                if light[j]:
                    break
                light[j] = 1
    for i in range(n):
        if not light[i]:
            return False
    return True # 다 비출 수 있음

s, e = 0, n
while (s <= e):
    mid = (s+e)//2
    if can(mid) and not can(mid-1):
        break
    if can(mid):
        e = mid
    else:
        s = mid+1
print(mid)