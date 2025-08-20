import sys, math
input = sys.stdin.readline

n = int(input())
m = int(input())
data = list(map(int, input().split()))

first = data[0]
last = n - data[-1]
mid = 0
for i in range(m-1):
    mid = max(mid, math.ceil((data[i+1] - data[i])/2))
print(max(first, last, mid))

# def can(h):
#     road = [0]*n
#     for i in range(m):
#         loc = data[i]
#         for l in range(loc-1, max(-1, loc-h-1), -1):
#             if road[l]:
#                 break
#             road[l] = 1
#         for r in range(loc, min(loc+h, n)):
#             if road[r]:
#                 break
#             road[r] = 1
#     for i in range(len(road)):
#         if not road[i]:
#             return False
#     return True

# s, e = 1, n
# while (True):
#     mid = (s+e)//2
#     if can(mid) and not can(mid-1):
#         break
#     if can(mid):
#         e = mid
#     else:
#         s = mid+1
# print(mid)