# 음의 가중치 -> 플로이드 워셜, 벨만 포드
# 음의 사이클이 있는가? -> o. 음의 사이클이 있다면 사이클을 돌며 무한히 걸리는 가중치 줄어들 것
# 도시 500개 -> 125000000 (1억 이상) -> 시간 제한 1초이기에 플로이드-워셜 적합하지 않음
# 이용 알고리즘: 벨만 포드 
# 1번 -> n번 도시 이동에서 음의 사이클이 존재하면 -1 반환
# 모든 간선을 v-1번 탐색, 음수 사이클의 존재 여부를 확인하려면 1번 더 탐색
# 탐색 시, 도착지까지의 시간이 기존보다 더 작아지면 업데이트

import sys
import collections
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
edges = []
shortest = [-1] * (n+1)
visited = [0] * (n+1)
shortest[1] = 0
visited[1] = 1
for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

for _ in range(n-1):
    for i in range(len(edges)):
        start, end, weight = edges[i][0], edges[i][1], edges[i][2]
        if not visited[start]:
            continue
        if not visited[end]:
            visited[end] = 1
            shortest[end] = shortest[start]+weight
        elif shortest[start]+weight < shortest[end]:
            shortest[end] = shortest[start]+weight


inf_cycle = False
for i in range(len(edges)):
    start, end, weight = edges[i][0], edges[i][1], edges[i][2]
    if not visited[start]:
        continue
    if shortest[start] + weight < shortest[end]:
        inf_cycle = True

if inf_cycle:
    print(-1)
else:
    for i in range(2,n+1):
        print(shortest[i])