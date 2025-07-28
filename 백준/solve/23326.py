import sys
input = sys.stdin.readline

n, q = map(int, input().split())
data = list(map(int, input().split()))

# segment tree 생성
tree = [0] * 4 * n

# 명소 정정
def change_good(start, end, idx, target):
    # base: 해당 명소 정정
    if start == end and start == target:
        tree[idx] = 1 if tree[idx] == 0 else 0
        return tree[idx]
    # recursive: 명소 재귀 정정하고 현위치 업데이트
    mid = (start+end)//2
    if target <= mid:
        half = change_good(start, mid, idx*2+1, target)
        tree[idx] = half + tree[idx*2+2]
    else:
        half = change_good(mid+1, end, idx*2+2, target)
        tree[idx] = half + tree[idx*2+1]
    return tree[idx]

# 현위치 변경
def change_loc(cur_loc, x):
    return (cur_loc + x) % n

# 명소까지의 최소 이동거리
def find_first(start, end, idx, target_s, target_e):
    if tree[idx] == 0:
        return -1
    if end < target_s:
        return -1
    if start == end and tree[idx] == 1:
        return start
    mid = (start+end)//2
    result_1 = find_first(start, mid, idx*2+1, target_s, target_e)
    if result_1 != -1:
        return result_1
    return find_first(mid+1, end, idx*2+2, target_s, target_e)

for i in range(n):
    if data[i] == 1:
        change_good(0, n-1, 0, i)

cur_loc = 0
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        change_good(0, n-1, 0, query[1]-1)
    elif query[0] == 2:
        cur_loc = change_loc(cur_loc, query[1])
    else:
        result_1 = find_first(0, n-1, 0, cur_loc, n-1)
        if result_1 != -1:
            # 가장 가까운 위치: result_1
            distance = result_1 - cur_loc
            print(distance)
            continue
        result_2 = find_first(0, n-1, 0, 0, cur_loc-1)
        if result_2 == -1:
            print(result_2)
            continue
        distance = result_2 + n - cur_loc
        print(distance)