# 모든 케이스 통과! 시간 짧지만 코드가 복잡..

def giright(x,y,bo,gi): # 삭제시 기둥 조건 만족 함수.
    if (x,y) in gi:
        if y == 0 or (x,y-1) in gi or (x-1,y) in bo or (x,y) in bo:
            return True
        else:
            return False
    else:
        return True
    
def boright(x,y,bo,gi): # 삭제시 보 조건 만족 함수.
    if (x,y) in bo:
        if (x,y-1) in gi or (x+1,y-1) in gi or ((x-1,y) in bo and (x+1,y) in bo):
            return True
        else:
            return False
    else:
        return True

def solution(n, build_frame):
    b = len(build_frame)
    gi = [] 
    bo = []
    for index in range(b):
        x = build_frame[index][0]
        y = build_frame[index][1]
        what = build_frame[index][2] # 기둥인지 보인지?
        build_delete = build_frame[index][3] # 설치할지 삭제할지?
        
        if what == 0: # 기둥이라면
            if build_delete == 1: # 설치한다면 
                if y == 0 or (x,y-1) in gi or (x-1,y) in bo or (x,y) in bo: # 조건 만족
                    gi.append((x,y))
            else: # 삭제한다면
                gi.remove((x,y)) # 우선 삭제하고
                if boright(x-1,y+1,bo,gi)==True and boright(x,y+1,bo,gi)==True and giright(x,y+1,bo,gi)==True:
                    pass # 조건 성립하면 삭제 납둔다
                else: # 조건이 성립하지 않으면
                    gi.append((x,y)) # 다시 더한다
                
        else: # 보라면
            if build_delete == 1: # 설치한다면
                if (x,y-1) in gi or (x+1,y-1) in gi or ((x-1,y) in bo and (x+1,y) in bo):
                    bo.append((x,y))
            else: # 삭제한다면
                bo.remove((x,y)) # 우선 삭제
                if boright(x-1,y,bo,gi)==True and boright(x+1,y,bo,gi)==True and giright(x,y,bo,gi)==True and giright(x+1,y,bo,gi)==True:
                    pass
                else:
                    bo.append((x,y))
    result = []
    for i in gi:
        ii = list(i)
        ii.append(0)
        result.append(ii)

    for i in bo:
        ii = list(i)
        ii.append(1)
        result.append(ii)

    result.sort() 
    return result