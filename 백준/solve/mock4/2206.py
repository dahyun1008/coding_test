import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(input().strip())

dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
queue = deque()
visited_through = [[0]*m for _ in range(n)]
visited_not = [[0]*m for _ in range(n)]
queue.append((0, 0, 0, 1))

visited_not[0][0] = 1
visited_through[0][0] = 1
result = 0
find = False

while queue:
    node = queue.popleft()
    if node[0] == n-1 and node[1] == m-1:
        result = node[3]
        find = True
        break
    usedThrough = node[2]
    for i in range(4):
        next_r = node[0] + dir[i][0]
        next_c = node[1] + dir[i][1]

        if 0 <= next_r < n and 0 <= next_c < m:
            if data[next_r][next_c] == '0':
                if usedThrough:
                    if not visited_not[next_r][next_c] and not visited_through[next_r][next_c]:
                        queue.append((next_r, next_c, usedThrough, node[3]+1))
                        visited_through[next_r][next_c] = 1
                else:
                    if not visited_not[next_r][next_c]:
                        queue.append((next_r, next_c, usedThrough, node[3]+1))
                        visited_through[next_r][next_c] = 1
                        visited_not[next_r][next_c] = 1
            elif not usedThrough and not visited_through[next_r][next_c]: # 벽이고 아직 기회 남은 경우
                queue.append((next_r, next_c, 1, node[3]+1))
                visited_through[next_r][next_c] = 1

if find:
    print(result)
else:
    print(-1)