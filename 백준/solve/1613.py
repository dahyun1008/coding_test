import sys

input = sys.stdin.readline
n, k = map(int, input().split())
order = [[0] * (401) for _ in range(401)]

def mark_order(prev, later):
    #  a - b라면 order[a][b] = 1
    order[prev][later] = 1

def check_order(first, second):
    if order[first][second] == 1: # first - second
        return -1
    elif order[second][first] == 1: # second - first
        return 1
    return 0

for _ in range(k):
    prev, later = map(int, input().split())
    mark_order(prev, later)

# i - k, k - j인 상황에서 i - j도 표현
# 반복 횟수: 6400 0000
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if order[i][k] == 1 and order[k][j] == 1: # a - b, b - c인 상황, a - c 표현
                order[i][j] = 1
            
s = int(input())

for _ in range(s):
    cand1, cand2 = map(int, input().split())
    print(check_order(cand1, cand2))