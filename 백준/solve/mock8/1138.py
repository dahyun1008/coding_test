import sys

input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))

loc = [0] * n
result = [0] * n

for i in range(n):
    idx = data[i]
    
    if i != 0:
        prev_list = loc[:i]
        prev_list.sort()
        # prev_list = sorted(loc[:i])
        
        for prev in prev_list:
            if prev <= idx:
                idx += 1
    loc[i] = idx
    result[idx] = i+1

print(' '.join(str(i) for i in result))