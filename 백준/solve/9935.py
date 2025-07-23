import sys

input = sys.stdin.readline

data = list(input().strip())
target = list(input().strip())
target_length = len(target)
prev_length = -1 * target_length

stack = []

for i in data:
    # 데이터 붙이기
    stack.append(i)
    # 맨 마지막에 타겟이 있다면
    if target_length <= len(stack) and stack[prev_length:] == target:
        del stack[prev_length:]

if not stack:
    print('FRULA')
else:
    print(*stack, sep='')