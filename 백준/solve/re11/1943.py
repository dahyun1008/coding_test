import sys
input = sys.stdin.readline

def can(half, cand):
    possible = [0] * (half+1)
    for i in range(len(cand)):
        cur = cand[i]
        if half < cur:
            continue
        if cur == half:
            return True
        if possible[half]:
            return True
        for j in range(half, -1, -1):
            if possible[j] and j + cur == half:
                return True
            elif possible[j] and j + cur < half:
                possible[j+cur] = 1
        possible[cur] = 1
    if possible[half]:
        return True
    return False


for _ in range(3):
    n = int(input())

    total = 0
    # 이진 분할
    cand = []
    for _ in range(n):
        price, count = map(int, input().split())
        total += price * count
        unit = 1
        while count > 0:
            if count - unit >= 0:
                cand.append(price*int(unit))
                count -= unit
                unit *= 2
            else:
                cand.append(price*count)
                count = 0
                
    # 절반 만들기
    half = total//2
    if total % 2:
        print(0)
    else:
        if can(half, cand):
            print(1)
        else:
            print(0)
    