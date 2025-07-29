import sys

input = sys.stdin.readline

n, m = map(int, input().split())
guitar_can = []
total_can = [0] * m
total_can_count = 0

for _ in range(n):
    _, can = input().split()
    can_list = []
    for i in range(m):
        if can[i] == 'Y':
            can_list.append(i)
            if total_can[i] == 0:
                total_can[i] = 1
                total_can_count += 1
    guitar_can.append(set(can_list))

condition = set(range(m))

# 최대한 많은 곡을 제대로 연주하려고 한다
# 최대한 많은 곡을 연주할 수 있는 개수 중 최소 개수를 구해야 함
# 연주할 수 있는 최대한 많은 곡: total_can_count
# 최선을 다해도 남기게 되는 곡의 개수: m - total_can_count
# condition: 남은 개수, idx: 이번에 선택할지 고민 중인 기타의 인덱스 번호, amount: 지금까지 선택한 기타
def recur(condition, idx, amount):
    if len(condition) <= m - total_can_count:
        return amount
    if n <= idx:
        return 11
    # 현재의 기타 idx를 선택하거나 선택하지 않는다
    
    ack = recur(condition - guitar_can[idx], idx+1, amount+1)
    nack = recur(condition, idx+1, amount)
    return min(ack, nack)

if total_can_count == 0:
    print(-1)
else:
    print(recur(condition, 0, 0))