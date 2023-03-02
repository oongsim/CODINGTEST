def solution(N, stages):
    cnt = [0] * (N+2) # 계수정렬 이용
    fail_rate = [] # 실패율 리스트
    for i in range(len(stages)):
        cnt[stages[i]] += 1
        
    for i in range(1, N+1):
        fail_rate.append((i, cnt[i]/sum(cnt[i:])))
    
    fail_rate.sort(key=lambda x:(-x[1], x[0])) # 실패율 기준 내림차순, 같으면 스테이지 오름차순
    
    result = []
    for i in fail_rate:
        result.append(i[0])
        
    return result