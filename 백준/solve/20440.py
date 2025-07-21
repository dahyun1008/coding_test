import sys
from collections import defaultdict

input = sys.stdin.readline

time = defaultdict(int)

n = int(input())
for _ in range(n):
    s, e = map(int, input().split())
    time[s]+=1
    time[e]-=1

sorted_time = sorted(time)

max, max_s, max_e = 0, 0, 0
now_max = False

# 7에 대해 구할 때, 98 업데이트 -> 98을 끝으로 표시도 함 

for i in range(len(sorted_time)-1):
    time[sorted_time[i+1]] += time[sorted_time[i]]
    if max < time[sorted_time[i]]:
        now_max = True
        max, max_s = time[sorted_time[i]], sorted_time[i]
    if now_max and time[sorted_time[i+1]] < time[sorted_time[i]]:
        now_max = False
        max_e = sorted_time[i+1]

print(max)
print(f"{max_s} {max_e}")