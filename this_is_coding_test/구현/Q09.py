def solution(s):
    mi = 1000 # 처음 최소값 저장
    for i in range(1, len(s)+1): # i는 자르는 개수
        n = len(s) // i
        c = 1
        r = []
        for j in range(n-1): # 비교
            if s[i*j : i*j+i] == s[i*j+i : i*j+2*i]:
                c += 1
            else:
                r.append(str(c))
                r.append(s[i*j : i*j+i])
                c = 1
        r.append(str(c)) # 비교하고 남은 뒷부분 처리
        r.append(s[i*(n-1) :])
        r = ''.join(r) # 리스트를 문자열로
        r = r.replace('1','') # 1은 없애준다
        # r에 문자열 완성
        
        m = len(r) # 현재 문자열 길이 m 에 저장
        mi = min(m, mi) # m 와 mi 중 작은값 mi에 저장      
    return mi