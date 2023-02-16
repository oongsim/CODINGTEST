# 책 풀이

from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = 10000 # 처음 친구 수 최소값 초기화
    
    # index를 이용하여 취약점을 하나하나 맨 처음 검사 시작하는 시작점으로 설정.  
    for start in range(length):
        # 모든 친구가 나열된 순열 조합에 대하여 확인
        for friends in list(permutations(dist,len(dist))):
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count-1]     
            # 시작점부터 모든 취약 지점을 확인
            for index in range(start, start+length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count-1] # 마지막 위치
            answer = min(answer, count) # 모든 순열 조합 중 최솟값 계산
        
    if answer > len(dist): # 친구들을 모두 투입해도 취약 지점을 전부 점검할 수 없는 경우
        return -1
    
    return answer