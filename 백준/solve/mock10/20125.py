import sys

input = sys.stdin.readline
n = int(input())
data = []
for _ in range(n):
    data.append(input().strip())

row, col = 0, 0
stop = False
for i in range(n):
    for j in range(n):
        if data[i][j] == '*':
            row, col = i, j
            stop = True
            break
    if stop:
        break
heart_r, heart_c = row+2, col+1
mid_r, mid_c = row+1, col # 심장의 인덱스

length = 1

while mid_c - length >= 0 and data[mid_r][mid_c-length]=='*':
    length += 1
l_arm = length - 1

length = 1
while mid_c + length < n and data[mid_r][mid_c+length]=='*':
    length += 1
r_arm = length - 1

# 허리
length = 1
while mid_r - length < n and data[mid_r+length][mid_c] =='*':
    length += 1
w = length - 1

# 왼 다리
weist = mid_r + w # 허리 마지막 지점
length = 1
while weist+length < n and data[weist+length][mid_c-1]=='*':
    length += 1
l_leg = length - 1

# 오른 다리
length = 1
while weist+length < n and data[weist+length][mid_c+1]=='*':
    length += 1
r_leg = length - 1

print(heart_r, heart_c)
print(l_arm, r_arm, w, l_leg, r_leg)