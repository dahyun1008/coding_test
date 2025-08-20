import sys
input = sys.stdin.readline
n = int(input())

data = []
for _ in range(n):
    data.append((list(map(int, input().split()))))

def recur(idx, data, count):
    if idx == len(data):
        return count
    
    if data[idx][0] <= 0:
        return recur(idx+1, data, count)
    
    result = count
    
    for i in range(len(data)):
        if idx == i:
            continue
        
        if data[i][0] <= 0:
            continue

        # i번 계란과 깬다
        data[idx][0] -= data[i][1]
        data[i][0] -= data[idx][1]
        broken_idx = False
        broken_i = False

        if data[i][0] <= 0:
            count += 1
            broken_i = True
        if data[idx][0] <= 0:
            count += 1
            broken_idx = True
        
        cur = recur(idx+1, data, count)
        result = max(result, cur)

        data[idx][0] += data[i][1]
        data[i][0] += data[idx][1]

        if data[i][0] > 0 and broken_i:
            count -= 1
        if data[idx][0] > 0 and broken_idx:
            count -= 1
    
    return result

print(recur(0, data, 0))