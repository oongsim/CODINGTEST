# 균형잡힌 괄호 문자열의 인덱스 반환
def balanced_index(s):
    cnt = 0 # 왼쪽 ( 의 개수
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        elif s[i] == ')':
            cnt -= 1
        if cnt == 0:
            return i
        
# 올바른 괄호 문자열인지 확인
def check_right(s):
    cnt = 0 # 왼쪽 ( 의 개수
    for i in s:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0: # 짝이 맞지 않은 경우에 False 반환
                return False
            cnt -= 1
    return True # 균형잡힌 괄호 문자열인 경우에만 검사하므로 끝까지 가면 모두 cnt == 0 인 상태로 True 반환


def solution(p):
    answer = ''
    # 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if p == '':
        return answer
    
    # 문자열 p를 '균형잡힌 문자열' u,v로 분리 
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]
    
    # 수행한 결과 문자열을 u에 이어 붙인 후 반환
    # 문자열 u가 '올바른 괄호 문자열'이면 문자열 v에 대해 처음부터 수행
    if check_right(u) == True:
        answer = u + solution(v)
        
    # 문자열 u가 '올바른 괄호 문자열'이 아니라면
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        #u = u[1:-1]
        #u = "".join(reversed(u))
        #answer += u
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
    return answer