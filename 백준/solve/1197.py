import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())
edges = []

for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

con_num = 0
min_weight = 0
root = [i for i in range(V+1)]

def find(x):
    if root[x] == x:
        return root[x]
    root[x] = find(root[x])
    return root[x]

for i in range(E):
    if con_num == V-1:
        break

    c, a, b = edges[i]
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        continue

    con_num += 1
    min_weight += c

    if root_a < root_b:
        root[root_b] = root_a
    else:
        root[root_a] = root_b

print(min_weight)