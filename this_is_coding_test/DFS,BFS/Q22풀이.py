from collections import deque

# 이동할 수 있는 위치 확인 하는 함수
def get_next_pos(pos, board):
    next_pos = [] # 반환 결과(이동 가능한 위치들)
    pos = list(pos) # 현재 위치 정보를 리스트로 변환(집합 -> 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    
    # 상, 하, 좌, 우 로 이동하는 경우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_nx = pos1_x + dx[i]
        pos1_ny = pos1_y + dy[i]
        pos2_nx = pos2_x + dx[i]
        pos2_ny = pos2_y + dy[i]
        # 이동하고자 하는 두 칸이 모두 비어있다면
        if board[pos1_nx][pos1_ny] == 0 and board[pos2_nx][pos2_ny] == 0:
            next_pos.append({(pos1_nx,pos1_ny),(pos2_nx,pos2_ny)})
            
    # 회전 하는 경우
    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]: # 위쪽으로 회전하거나, 아래쪽으로 회전
            # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
            if board[pos1_x+i][pos1_y] == 0 and board[pos2_x+i][pos2_y] == 0:
                next_pos.append({(pos1_x,pos1_y),(pos1_x+i,pos1_y)})
                next_pos.append({(pos2_x,pos2_y),(pos2_x+i,pos2_y)})      
    # 현재 로봇이 세로로 놓여 있는 경우 
    elif pos1_y == pos2_y:
        for i in [-1, 1]: # 왼쪽으로 회전하거나, 오른쪽으로 회전
            # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
            if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0:
                next_pos.append({(pos1_x,pos1_y),(pos1_x,pos1_y+i)})
                next_pos.append({(pos2_x,pos2_y),(pos2_x,pos2_y+i)})
            
    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos


def solution(board):
    n = len(board)
    newboard =  [[1]*(n+2) for _ in range(n+2)] # 외각에 벽이 둘러싼 맵 생성
    for i in range(n):
        for j in range(n):
            newboard[i+1][j+1] = board[i][j]
            
    # bfs 수행
    q = deque()
    visited = [] # 방문 리스트
    pos = {(1,1),(1,2)} # 현재 위치
    q.append((pos,0)) # (현재 위치, 시간)을 큐에 넣기 
    visited.append(pos) # 방문 처리
    
    while q: # 큐가 빌 때 까지
        pos, time = q.popleft() # 큐에서 하나 꺼낸다
        # (n,n) 위치에 로봇이 도달했다면, 최단거리이므로 반환 
        if (n,n) in pos:
            return time
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, newboard):
            # 아직 방문하지 않은 위치라면 큐에 넣고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, time+1))
                visited.append(next_pos)
    return 0