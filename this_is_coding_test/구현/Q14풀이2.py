# 유튜브 풀이, 더 이해하기 쉬운 것 같기도

from itertools import permutations
import math

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    weakSize = len(weak)
    weak = weak + [w+n for w in weak]
    minCnt = math.inf # 처음 친구 수 최소값 초기화
    
    # index를 이용하여 취약점을 하나하나 맨 처음 검사 시작하는 시작점으로 설정.  
    for start in range(weakSize):
        # 모든 친구가 나열된 순열 조합에 대하여 확인
        for d in permutations(dist,len(dist)):
            cnt = 1
            pos = start # 현재 친구의 시작점이 pos
            for i in range(1, weakSize): # 처음은 이미 방문했으므로 1부터 시작
                nextPos = start + i # pos, nextPos 모두 인덱스 값
                diff = weak[nextPos] - weak[pos] # 거리
                if diff > d[cnt-1]: # weak 간격 거리보다 친구가 갈 수 있는 거리가 작으면
                    pos = nextPos # 시작위치를 nextPos로 바꾸고
                    cnt += 1 # 친구 한 명 추가
                    if cnt > len(dist): # 친구가 초과되면 break
                        break
            if cnt <= len(dist): # 친구가 초과될 경우 최소값 비교도 하지 못함
                minCnt = min(minCnt, cnt)
    
    if minCnt == math.inf: # 모두 친구가 초과되어 값을 구하지 못한 경우
        return -1

    return minCnt