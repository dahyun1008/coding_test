import sys
n = int(sys.stdin.readline())

amount = 1 # layer 번호
total = 1 # 커버되는 방의 끝 번호

while n > total:
    amount += 1
    total += (amount - 1) * 6

print(amount)