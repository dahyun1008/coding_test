import sys
import bisect

input = sys.stdin.readline
# n: row, m: col, l: width, k: number
n, m, l, k = map(int, input().split())

stars = []
for i in range(k):
    stars.append(tuple(map(int, input().split())))

dir = [(-l, -l), (l, -l), (-l, l), (l, l)]

stars.sort()
max_result = 0
for i in range(k):
    origin = (stars[i][0], stars[i][1])
    for j in range(4):
        left_top = (min(origin[0], max(0, origin[0]+dir[j][0]), n-l), 
                    min(origin[1], max(0, origin[1]+dir[j][1]), m-l))
        right_bottom = (min(left_top[0]+l, n), min(left_top[1]+l, m))
        idx_first = bisect.bisect_left(stars, left_top)
        idx_last = bisect.bisect_right(stars, right_bottom)
        cur = 0
        for t in range(idx_first, idx_last):
            if left_top[1] <= stars[t][1] <= right_bottom[1]:
                cur+=1
        max_result = max(max_result, cur)
        

print(k-max_result)