import sys

input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []
l, n = input().split()
rooms.append([(n, int(l))])
for i in range(1, p):
    l, n = input().split()
    l = int(l)
    joined = False
    for r in range(len(rooms)):
        if len(rooms[r]) < m and rooms[r][0][1]-10 <= l <= rooms[r][0][1]+10:
            joined = True
            rooms[r].append((n, l))
            break
    if not joined:
        rooms.append([(n, l)])

for r in range(len(rooms)):
    if len(rooms[r]) == m:
        print("Started!")
    else:
        print("Waiting!")
    rooms[r].sort()
    for people in rooms[r]:
        print(people[1], people[0])