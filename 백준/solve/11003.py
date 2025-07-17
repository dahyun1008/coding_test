import sys
from collections import deque

input = sys.stdin.readline
n, l = map(int, input().split())

data = list(map(int, input().split()))
result = []
ds = deque()
start, end = -l+1, 0

while start <= 0:
    # 추가하려는게 기존 것보다 작으면 기존거 팝, 크면 그냥 추가
    while ds and data[ds[-1]] >= data[end]:
        ds.pop()
    ds.append(end)
    result.append(data[ds[0]])

    start += 1
    end += 1

while end < n:
    # 슬라이딩 왼도우 크기 넘은거 지우기
    while ds and ds[0] < start:
        ds.popleft()
    
    # 추가하려는게 기존 것보다 작으면 기존거 팝, 크면 그냥 추가
    while ds and data[ds[-1]] >= data[end]:
        ds.pop()
        
    ds.append(end)
    result.append(data[ds[0]])
    
    start += 1
    end += 1


print(" ".join(str(i) for i in result))