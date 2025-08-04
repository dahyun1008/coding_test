from typing import List

asset_list = dict({"SP": 0, "KE": 1, "MO": 2, "CO": 3, "DE": 4})

# 유효성 파악 함수 (인자는 각 필드 단위 분리된 튜플로 제공)
# 반환값: 유효(1), 유효하지 않음(-1)
def validation(data):
    if data[0] < 13 or data[0] > 22:
        return -1
    if data[1] not in asset_list.keys():
        return -1
    if data[2] < 1 or data[2] > 12:
        return -1
    if data[3] < 1 or data[3] > 99:
        return -1
    return 1

# 파싱 함수
# 반환값: (연도: int, 자산 코드: str, 등록월: int, 순서: int)
def parsing(data):
    year, remain = data.split('-')
    return (int(year), remain[:2], int(remain[2:4]), int(remain[4:]))

# 비교 함수
# 반환값: target이 더 크면(더 나중이면) 1, 작으면 -1
def is_bigger(target_raw, compare_raw):
    target = parsing(target_raw)
    compare = parsing(compare_raw)

    # 연도로 비교
    if target[0] > compare[0]:
        return 1
    elif target[0] < compare[0]:
        return -1
    
    # 자산 코드로 비교
    if asset_list[target[1]] > asset_list[compare[1]]:
        return 1
    elif asset_list[target[1]] < asset_list[compare[1]]:
        return -1
    
    # 등록 월로 비교
    if target[2] > compare[2]:
        return 1
    elif target[2] < compare[2]:
        return -1
    
    # 등록 순서 비교
    if target[3] > compare[3]:
        return 1
    elif target[3] < compare[3]:
        return -1
    
    return 0 # 동일한 경우

def insert(result, cur_asset):
    if len(result) == 0:
        result.append(cur_asset)
        return

    # 이진 탐색을 통해 위치 찾기
    left, right = 0, len(result)
    same = False

    while left < right:
        mid = (left + right) // 2
        bigger = is_bigger(result[mid], cur_asset)
        if bigger == 1: # mid가 더 큰 경우
            right = mid
        elif bigger == -1:
            left = mid + 1
        else:
            same = True
            break
    if same:
        return
    
    result.insert(left, cur_asset)
    
    

def solution(assets: List[str]) -> List[str]:
    result = []
    for i in range(len(assets)):
        if validation(parsing(assets[i])) == -1:
            continue
        insert(result, assets[i])
    return result

print(solution(["20-DE0815", "20-CO1299", "20-MO0901", "20-KE0511", "20-SP1102","21-DE0401", "21-CO0404", "21-MO0794", "21-KE0704", "21-SP0404","19-DE0401", "19-CO0404", "19-MO0794", "19-KE1204", "19-SP0404"]))

print(solution(["2-MO0915", "19-MO1299", "17-CO0901", "14-DE0511", "19-KE1102", "13-DE0101", "20-SP0404", "20-CO0794"]))

print(solution(["13-DE0401", "13-DE0401", "22-MO0815", "19-MO1299", "17-CO0901", "14-DE0511", "19-KE1102", "20-SP0404", "20-CO0794"]))