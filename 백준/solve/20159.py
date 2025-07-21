import sys

input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))

sum = 0
for i in range(0, len(cards), 2):
    sum += cards[i]

max_sum = sum
sum2 = sum

for i in range(len(cards)-1, 0, -2):
    sum += cards[i]
    sum -= cards[i-1]
    max_sum = max(max_sum, sum)

for i in range(len(cards)-2, 0, -2):
    sum2 -= cards[i]
    sum2 += cards[i-1]
    max_sum = max(max_sum, sum2)

print(max_sum)