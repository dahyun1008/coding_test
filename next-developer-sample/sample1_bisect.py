import bisect

def valid_year(year):
    if 13 <= year <= 22:
        return True
    return False

def valid_code(code):
    if len({code} & {"SP", "KE", "MO", "CO", "DE"}) == 1:
        return True
    return False

def valid_month(year, month):
    if year == 13:
        if 4 <= month <= 12:
            return True
        return False
    if year == 2:
        if 1 <= month <= 8:
            return True
        return False
    if 1 <= month <= 12:
        return True
    return False

def valid_order(order):
    if 1<=order<=99:
        return True
    return False

def valid_case(case):
    if case[2] == "-" and valid_year(int(case[:2])) and len(case[3:]) == 6 and valid_code(case[3:5]) and valid_month(int(case[:2]), int(case[5:7])) and valid_order(int(case[7:9])):
        return True
    return False

codes = {"SP": 1, "KE": 2, "MO": 3, "CO": 4, "DE": 5}
def convert_num(case):
    return (int(case[:2]), codes[case[3:5]], int(case[5:7]), int(case[7:9]))

def solution(data):
    result_data = []
    result = []
    for case in data:
        if not valid_case(case):
            continue
        case_data = convert_num(case)
        if len({case_data} & set(result_data)) == 1:
            continue
        idx = bisect.bisect_left(result_data, case_data)
        result_data.insert(idx, case_data)
        result.insert(idx, case)
    print(result)

# solution(["20-DE0815", "20-CO1299", "20-MO0901", "20-KE0511", "20-SP1102","21-DE0401", "21-CO0404", "21-MO0794", "21-KE0704", "21-SP0404","19-DE0401", "19-CO0404", "19-MO0794", "19-KE1204", "19-SP0404"])
print()
solution(["2-MO0915", "19-MO1299", "17-CO0901", "14-DE0511", "19-KE1102", "13-DE0101", "20-SP0404", "20-CO0794"])
print()
# solution(["13-DE0401", "13-DE0401", "22-MO0815", "19-MO1299", "17-CO0901", "14-DE0511", "19-KE1102", "20-SP0404", "20-CO0794"])