def rotation(lst): # 2차원 리스트 90도 회전
    n = len(lst) # 행 길이 계산
    m = len(lst[0]) # 열 길이 계산
    result = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[j][n-1-i] = lst[i][j]
    return result

def check(lst): # 자물쇠의 중간 부분이 모두 1인지 확인
    n = len(lst) // 3
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if lst[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    # 자물쇠의 크기를 기존의 3배로 변환. n >= m 이므로 최대 경우로.
    nlock = [[0]*(3*n) for _ in range(3*n)]
    # 새로운 자물쇠의 중앙 부분에 기존의 좌물쇠 넣기
    for i in range(n):
        for j in range(n):
            nlock[n+i][n+j] = lock[i][j]
    
    for _ in range(4): # 4가지 방향에 대해서 확인
        key = rotation(key) # 열쇠 회전
        for x in range(n*2): # x,y 좌표 범위를 n*2 까지로 해야 i,j 더했을때 전체 검색 가능
            for y in range(n*2):
                # 자물쇠에 열쇠 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        nlock[x+i][y+j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(nlock) == True:
                    return True
                # 자물쇠에서 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        nlock[x+i][y+j] -= key[i][j]
    return False