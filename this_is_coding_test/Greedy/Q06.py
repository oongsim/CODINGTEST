def solution(food_times, k):
    count = min(food_times) * len(food_times) # 최소시간 * 총 개수
    
    if k < count : # k가 최소시간 * 총 개수 보다 작을 때 
        k -= count
        a = (len(food_times) - abs(k)) % len(food_times)
        return abs(a)+1
    
    else:
        k -= count # 남은 시간
        rfood_times = [food_times[i] - min(food_times) for i in range(len(food_times))]
        # 남은 food_times

        lst = [] 
        for i in range(len(rfood_times)):
            lst.append([i+1,rfood_times[i]]) # [번호, 남은 시간] 으로

        while(True):
            for i in lst:
                if k == 0:
                    return i[0]
                if i[1] > 0:
                    k -= 1
                    i[1] -= 1

            llst = [i[1] for i in lst]
            if llst == [0 for i in range(len(lst))]: # 더 섭취할 음식이 없을 때 -1 반환
                return -1