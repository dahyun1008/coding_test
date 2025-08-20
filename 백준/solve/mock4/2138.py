import sys, copy

input = sys.stdin.readline

n = int(input())
str_data = input().strip()
data = []
for i in range(len(str_data)):
    data.append(int(str_data[i]))

data_copy = copy.deepcopy(data) # 인덱스 0 스위치 킨 경우 이용 용도
str_target = input().strip()

target = []
for i in range(len(str_target)):
    target.append(int(str_target[i]))

# 인덱스 0 스위치 끈 경우
count = 0
for i in range(1, n):
    if data[i-1] != target[i-1]:
        count += 1
        for j in range(i-1, min(i+2, n)):
            data[j] = 1 if not data[j] else 0
if data[-1] != target[-1]:
    count = -1

# 인덱스 0 스위치 킨 경우
data_copy[0] = 1 if not data_copy[0] else 0
data_copy[1] = 1 if not data_copy[1] else 0

count_copy = 1
for i in range(1, n):
    if data_copy[i-1] != target[i-1]:
        count_copy += 1
        for j in range(i-1, min(i+2, n)):
            data_copy[j] = 1 if not data_copy[j] else 0
if data_copy[-1] != target[-1]:
    count_copy = -1

if count == -1 and count_copy == -1:
    print(-1)
elif count == -1:
    print(count_copy)
elif count_copy == -1:
    print(count)
else:
    print(min(count, count_copy))