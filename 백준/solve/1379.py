import sys
import heapq

input = sys.stdin.readline

n = int(input())
result = [0] * n
rooms = []
data = []
room_num = 1

for _ in range(n):
    lacture_num, start_time, end_time = map(int, input().split())
    data.append((start_time, end_time, lacture_num))
data.sort()

for i in range(n):
    number, start, end = data[i][2], data[i][0], data[i][1]
    if len(rooms) == 0 or rooms[0][0] > start:
        heapq.heappush(rooms, (end, room_num))
        result[number-1] = room_num
        room_num += 1
    else:
        _, alloc_room = heapq.heappop(rooms)
        heapq.heappush(rooms, (end, alloc_room))
        result[number-1] = alloc_room

print(room_num-1)
for i in result:
    print(i)