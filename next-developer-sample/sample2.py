# 멋쟁이 숫자 중 999를 발견한 경우, 더 탐색할 필요 없다
# 모두 탐색하고 정렬했을때, 멋쟁이 숫자가 1종류뿐이고, 000이라면 0을 리턴
# 멋쟁이 숫자가 없다면 -1을 리턴
# 길이 5라면, 0~4 -> 시작점: 2(range 끝 범위: 3) -> 길이 - 2
def solution(str_data):
    cool_nums = []

    for i in range(len(str_data)-2):
        substring = str_data[i:i+3]
        same = True
        for j in range(1,3):
            if substring[0] != substring[j]:
                same = False
                break
        if same:
            cool_nums.append(int(substring))

    cool_nums.sort()
    if len(cool_nums) == 0:
        return -1
    if len(cool_nums) == 1 and cool_nums[0] == 000:
        return 0
    return cool_nums[-1]

print(solution("123"))