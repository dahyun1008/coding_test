import sys

input = sys.stdin.readline

def find(root, x):
    if x == root[x]:
        return root[x]
    root[x] = find(root, root[x])
    return root[x]

t = int(input())
for test in range(t): # 각각의 테스트 케이스에 대하여
    rows, cols = map(int, input().split())
    edges = []

    # 가로 간선 저장
    for r in range(rows):
        row = list(map(int, input().split()))
        for c in range(cols-1):
            edges.append((row[c], r*cols+c, r*cols+c+1))
    
    # 세로 간선 저장
    for r in range(rows-1):
        multi_row = list(map(int, input().split()))
        for c in range(cols):
            edges.append((multi_row[c], r*cols+c, (r+1)*cols+c))
    
    edges.sort()
    min_cost = 0
    nodes = rows *cols
    root = [i for i in range(nodes)]

    for i in range(len(edges)):
        weight, a, b = edges[i][0], edges[i][1], edges[i][2]
        root_a = find(root, a)
        root_b = find(root, b)

        if root_a != root_b:
            min_cost += weight
            if root_a < root_b:
                root[root_b] = root_a
            else:
                root[root_a] = root_b
    print(min_cost)