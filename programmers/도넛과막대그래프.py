from collections import defaultdict

def check_type(node, connect): # donut -> 1, line -> 2, eight -> 3
    cur = node
    start = node
    while len(connect[cur]) != 0:
        if len(connect[cur]) == 2:
            return 3
        # 다음 노드로 이동
        cur = connect[cur][0]
        # 이동했을 때, 제자리로 돌아오는가 (8자 그래프의 경우, 제자리로 돌아오기 위해 반드시 위 if 조건에 걸림)
        if cur == start:
            return 1
    return 2
    

def solution(edges):
    connect = defaultdict(list)
    come_count = [0] * 1000001
    
    added_node = 0
    for i in range(len(edges)):
        connect[edges[i][0]].append(edges[i][1])
        come_count[edges[i][1]] += 1
    
    for cand in range(1000001):
        if come_count[cand] == 0 and len(connect[cand]) >= 2:
            added_node = cand
            break
    
    donut, line, eight = 0, 0, 0
    
    for node in connect[added_node]: # 그래프 종류 확인하기
        if check_type(node, connect) == 1:
            donut += 1
        elif check_type(node, connect) == 2:
            line += 1
        else:
            eight += 1
        
    answer = [added_node, donut, line, eight]
    return answer