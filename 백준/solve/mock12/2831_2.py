import sys
input = sys.stdin.readline

n = int(input())

# 남자 입력
data = list(map(int, input().split()))
man_neg = []
man_pos = []
for i in range(n):
    if data[i] < 0:
        man_neg.append(-1*data[i])
    else:
        man_pos.append(data[i])

# 여자 입력
data = list(map(int, input().split()))
woman_neg = []
woman_pos = []
for i in range(n):
    if data[i] < 0:
        woman_neg.append(-1*data[i])
    else:
        woman_pos.append(data[i])

# 정렬
man_neg.sort()
man_pos.sort()
woman_neg.sort()
woman_pos.sort()

count = 0
man_idx, woman_idx = 0, 0
# 남자가 여자보다 키가 커야 한다
while man_idx < len(man_neg) and woman_idx < len(woman_pos):
    if man_neg[man_idx] > woman_pos[woman_idx]:
        count += 1
        man_idx += 1
        woman_idx += 1
    else:
        man_idx += 1

man_idx, woman_idx = 0, 0
# 여자가 남자보다 키가 커야 한다
while man_idx < len(man_pos) and woman_idx < len(woman_neg):
    if man_pos[man_idx] < woman_neg[woman_idx]:
        count += 1
        man_idx += 1
        woman_idx += 1
    else:
        woman_idx += 1
print(count)