import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
data = []
dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
for i in range(n):
    data.append(list(map(int, input().split())))

result = 1
for i in range(1, 100):
    safe_nodes = []
    safe = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if data[row][col] > i:
                safe[row][col] = 1
                safe_nodes.append((row, col))
    
    count = 0
    for node in safe_nodes:
        if visited[node[0]][node[1]]:
            continue
        count += 1
        queue = deque()
        queue.append((node[0], node[1]))
        visited[node[0]][node[1]] = 1
        while queue:
            (r, c) = queue.popleft()
            for i in range(4):
                next_r = r+dir[i][0]
                next_c = c+dir[i][1]
                if 0 <= next_r < n and 0 <= next_c < n and not visited[next_r][next_c] and safe[next_r][next_c]:
                    visited[next_r][next_c] = 1
                    queue.append((next_r, next_c))
    result = max(result, count)
print(result)