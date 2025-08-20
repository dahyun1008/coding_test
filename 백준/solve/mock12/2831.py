import sys
import bisect

input = sys.stdin.readline
n = int(input())

data_man = list(map(int, input().split()))
data_woman = list(map(int, input().split()))

man = [(-i, -1) if i < 0 else (i, 1) for i in data_man]
woman = [(-i, -1) if i < 0 else (i, 1) for i in data_woman]

man.sort()
woman.sort()
man_h, man_favor = [], []
woman_want_higher = []
woman_want_lower = []


for i in range(n):
    man_h.append(man[i][0])
    man_favor.append(man[i][1])
    if woman[i][1] == 1:
        woman_want_higher.append(woman[i][0])
    else:
        woman_want_lower.append(woman[i][0])

pair_woman_higher = [0] * len(woman_want_higher)
pair_woman_lower = [0] * len(woman_want_lower)

count = 0
woman_higher_index = n
woman_lower_index = 0 # 아직 짝 지어지지 않은 첫 번째 여자(작은 상대를 원함)
for i in range(n):
    if man_favor[i] == -1: # 작은 사람을 원함
        idx = bisect.bisect_left(woman_want_higher, man_h[i])
        idx = idx - 1
        idx = min(idx, woman_higher_index)
        
        while idx >= 0 and pair_woman_higher[idx]:
            idx -= 1
        if idx < 0:
            continue

        count += 1
        pair_woman_higher[idx] = 1
        woman_higher_index = idx - 1
        
    else: # 큰 사람을 원함
        idx = bisect.bisect_right(woman_want_lower, man_h[i])
        idx = max(idx, woman_lower_index)

        while idx < len(woman_want_lower) and pair_woman_lower[idx]:
            idx += 1
        if idx >= len(woman_want_lower):
            continue

        count += 1
        pair_woman_lower[idx] = 1
        woman_lower_index = idx+1

print(count)