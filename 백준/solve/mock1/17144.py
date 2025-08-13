import sys
from collections import deque
import pprint
from copy import deepcopy

input = sys.stdin.readline
R, C, T = map(int, input().split())
dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

data = []
for _ in range(R):
    data.append(list(map(int, input().split())))

conditionar = 0
for r in range(2, R-2):
    if data[r][0] == -1:
        conditionar = r
        break

queue = deque()
for r in range(R):
    for c in range(C):
        if data[r][c] > 0:
            queue.append((r, c))

for i in range(T):
    snapshoot = deepcopy(data)
    next = deque()
    while queue:
        (r, c) = queue.popleft()
        spread = snapshoot[r][c]//5
        amount = 0
        for i in range(4):
            if 0 <= r + dir[i][0] < R and 0 <= c + dir[i][1] < C and snapshoot[r + dir[i][0]][c + dir[i][1]] != -1:
                data[r + dir[i][0]][c + dir[i][1]] += spread
                amount += 1                  
        data[r][c] -= amount * spread

    
    # 순환
    con = conditionar
    for i in range(con-1, 0, -1):
        data[i][0] = data[i-1][0]

    # for i in range(C-1):
    #     data[0][i] = data[0][i+1]
    data[0][:C-1] = data[0][1:]
    for i in range(con):
        data[i][C-1] = data[i+1][C-1]

    # for i in range(C-1, 1, -1):
    #     data[con][i] = data[con][i-1]
    data[con][1:] = data[con][:C-1]
    
    for i in range(con+2, R-1):
        data[i][0] = data[i+1][0]
    # for i in range(0, C-1):
    #     data[R-1][i] = data[R-1][i+1]
    data[R-1][:C-1] = data[R-1][1:]
    for i in range(R-1, con+1, -1):
        data[i][C-1] = data[i-1][C-1]
    # for i in range(C-1, 1, -1):
    #     data[con+1][i] = data[con+1][i-1]
    data[con+1][1:] = data[con+1][:C-1]
    data[con][1] = 0
    data[con][0] = -1
    data[con+1][1] = 0
    data[con+1][0] = -1

    for next_r in range(R):
        for next_c in range(C):
            if data[next_r][next_c] > 0:
                queue.append((next_r, next_c))


result = 0
for i in range(R):
    for j in range(C):
        if data[i][j] > 0:
            result += data[i][j]

print(result)