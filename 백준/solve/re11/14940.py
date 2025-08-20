import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
distance = [[-1]*m for _ in range(n)]
target_r, target_c = 0, 0
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 0:
            distance[i][j] = 0
        elif temp[j] == 2:
            distance[i][j] = 0
            target_r, target_c = i, j

queue = []
heapq.heappush(queue, (0, (target_r, target_c)))

while queue:
    dis, (r, c) = heapq.heappop(queue)
    if distance[r][c] < dis:
        continue
    for i in range(4):
        next_r, next_c = r+dir[i][0], c+dir[i][1]
        if 0 <= next_r < n and 0 <= next_c < m and (distance[next_r][next_c] == -1 or dis + 1 < distance[next_r][next_c]):
            distance[next_r][next_c] = dis + 1
            heapq.heappush(queue, (dis+1, (next_r, next_c)))
            

for j in range(n):
    print(' '.join(str(i) for i in distance[j]))