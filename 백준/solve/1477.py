import sys
import heapq
input = sys.stdin.readline

n, m, l = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
data = [0] + data + [l]
dists = []
for i in range(n+1):
    dists.append(data[i+1]-data[i])
tree = [0] * 700

def seg_tree(node, start, end):
    if start == end:
        tree[node] = dists[start]
        return tree[node]
    mid = (start+end)//2
    left = seg_tree(2*node+1, 0, mid)
    right = seg_tree(2*node+2, mid+1, end)
    tree[node] = max(left, right)
    return tree[node]

seg_tree(0, 0, len(dists)-1)

def find_max():
    cur, start, end = 0, 0, len(dists)-1
    while(True):
        if tree[2*cur+1]==0 and tree[2*cur+2]==0:
            break
        if tree[2*cur+1] <= tree[2*cur+2]:
            cur = 2*cur+2
            start = (start+end)//2 + 1
        else:
            cur = 2*cur+1
            end = (start+end)//2
    return start, cur

for i in range(m):
    node_idx, tree_idx = find_max()