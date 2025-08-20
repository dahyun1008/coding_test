import sys
input = sys.stdin.readline
N, X = map(int, input().split())
data = list(map(int, input().split()))

total_sum, sum, count = 0, 0, 0

for i in range(X):
    sum += data[i]

for i in range(N-X):
    if total_sum == sum:
        count += 1
    elif total_sum < sum:
        total_sum = sum
        count = 1
    sum -= data[i]
    sum += data[i+X]

if total_sum == sum:
    count += 1
elif total_sum < sum:
    total_sum = sum
    count = 1

if total_sum == 0:
    print("SAD")
else:
    print(total_sum)
    print(count)