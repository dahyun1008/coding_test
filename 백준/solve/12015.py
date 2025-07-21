import sys
import bisect

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

inc = []

for number in a:
    idx = bisect.bisect_left(inc, number)
    if idx >= len(inc):
        inc.append(number)
    else:
        inc[idx] = number

print(len(inc))