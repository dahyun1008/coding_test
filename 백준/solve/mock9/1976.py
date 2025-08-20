import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
for i in range(n):
    data[i][i] = 1

plan = list(map(int, input().split()))

for mid in range(n):
    for s in range(n):
        for e in range(n):
            if data[s][mid] and data[mid][e]:
                data[s][e] = 1
                data[e][s] = 1

can = True
for i in range(m-1):
    if not data[plan[i]-1][plan[i+1]-1]:
        can = False
        break

if not can:
    print("NO")
else:
    print("YES")