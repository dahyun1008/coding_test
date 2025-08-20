import sys
input = sys.stdin.readline

T = int(input())

data = []
max_data = 0
for _ in range(T):
    cur = int(input())
    max_data = max(max_data, cur)
    data.append(cur)

Prime = [1] * max_data
Prime[0] = 0
Prime[1] = 0
for i in range(2, max_data):
    if Prime[i]:
        for j in range(i+i, max_data, i):
            Prime[j] = 0

prime_list = []
for i in range(max_data):
    if Prime[i]:
        prime_list.append(i)

for i in range(len(data)):
    count = 0
    for j in range(len(prime_list)):
        if prime_list[j] > data[i]/2:
            break
        if Prime[data[i]-prime_list[j]]:
            count += 1
    print(count)