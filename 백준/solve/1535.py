import sys
input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

value_per_weight = []

# 잃는 체력이 0
for i in range(n):
    if weights[i] == 0:
        value_per_weight.append((values[i], i))
    else:
        value_per_weight.append((values[i]/weights[i], i))
value_per_weight.sort(reverse=True)


# idx는 value_per_weight의 인덱스이고 실제 데이터 조회에는 value_per_weight[idx][1]인 실제 인덱스
def recursive(idx, happiness, remain_health):
    if remain_health <= 0:
        return 0
    if idx == n:
        return happiness
    ack = recursive(idx+1, happiness+values[value_per_weight[idx][1]], remain_health-weights[value_per_weight[idx][1]])
    nack = recursive(idx+1, happiness, remain_health)
    return max(ack, nack)

print(recursive(0, 0, 100))