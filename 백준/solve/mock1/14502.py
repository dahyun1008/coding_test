import sys
from copy import deepcopy
from collections import deque
from itertools import combinations

dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
input = sys.stdin.readline
n, m = map(int, input().split())
walls = []
for i in range(n):
    walls.append(list(map(int, input().split())))

initial_bad_list = []
wall_count = 0
emptys = []
for i in range(n):
    for j in range(m):
        if walls[i][j] == 1:
            wall_count += 1
        elif walls[i][j] == 0:
            emptys.append((i, j))
        else:
            initial_bad_list.append((i, j))

result = n * m

for combi in combinations(emptys, 3):
    for (r, c) in combi:
        walls[r][c] = 1 # 벽으로 만들기
    # 오염 세기
    data = deepcopy(walls)
    dirty_inc = 0
    queue = deque(initial_bad_list)

    while queue:
        (bad_r, bad_c) = queue.popleft()
        for i in range(4):
            next_r = bad_r + dir[i][0]
            next_c = bad_c + dir[i][1]
            if 0 <= next_r < n and 0 <= next_c < m and data[next_r][next_c] == 0:
                dirty_inc += 1
                data[next_r][next_c] = 2
                queue.append((next_r, next_c))
    result = min(result, dirty_inc)

    for (r, c) in combi:
        walls[r][c] = 0 # 빈 칸으로 되돌리기

print(n*m - wall_count - 3 - len(initial_bad_list) - result)