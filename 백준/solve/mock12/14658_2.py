import sys
import bisect

input = sys.stdin.readline
# n: row, m: col, l: width, k: number
n, m, l, k = map(int, input().split())

stars = []
stars_r, stars_c = set(), set()
for i in range(k):
    r, c = map(int, input().split())
    stars_r.add(r)
    stars_c.add(c)
    stars.append([r, c])

stars.sort()

max_result = 0
for r in stars_r:
    for c in stars_c:
        left_top = [min(r, n-l), min(c, m-l)]
        right_bottom = [left_top[0]+l, left_top[1]+l, m]
        idx_first = bisect.bisect_left(stars, left_top)
        idx_last = bisect.bisect_right(stars, right_bottom)
        cur = 0
        for t in range(idx_first, idx_last):
            if left_top[1] <= stars[t][1] <= right_bottom[1]:
                cur+=1
        max_result = max(max_result, cur)
        

print(k-max_result)