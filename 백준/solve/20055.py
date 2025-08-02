import sys

input = sys.stdin.readline

n, k = map(int, input().split())
balts = list(map(int, input().split()))

robot_loc = [0] * 2 * n
start, zero_count = 0, 0

# 로봇 이동 단계에서 zero_count 업데이트도
def move_robot(balts, robot_loc, start, zero_count):
    result = zero_count
    for i in range(n-1, 0, -1):
        loc = (start + i) % (2*n)
        next = (loc+1)%(2*n)
        if i == n-1: # 마지막 칸에서는 로봇을 꺼낸다
            if robot_loc[loc]:
                robot_loc[loc] = 0
            continue
        if robot_loc[loc] and not robot_loc[next] and balts[next] > 0:
            balts[next] -= 1
            if balts[next] == 0:
                result += 1
            robot_loc[next] = 1
            robot_loc[loc] = 0
    return result
        
cycle = 0
while True:
    cycle += 1
    start -= 1
    # 1단계 진행: 밸트 이동
    if start < 0:
        start = 2 * n - 1
    robot_loc[(start+n)%(2*n)] = 0

    # 2단계 진행: 로봇 이동
    zero_count = move_robot(balts, robot_loc, start, zero_count)

    if zero_count >= k:
        print(cycle)
        break

    # 3단계 진행: 새 로봇 올리기
    if balts[start] > 0:
        balts[start] -= 1
        robot_loc[start] += 1
        if balts[start] == 0:
            zero_count += 1
            if zero_count == k:
                print(cycle)
                break