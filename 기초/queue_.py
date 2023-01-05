from collections import deque
# deque는 스택, 큐 기능 모두 포함
# 첫번째 원소 제거 popleft() , 마지막 원소 제거 pop()
# 첫번째 인덱스에 원소 x 삽입 appendleft(x), 마지막 인덱스에 원소 삽입 append(X)

# 큐 자료구조 이용시, 삽입은 append(), 삭제는 popleft() 사용

data = deque([2,3,4])
data.append(5)
data.popleft()

print(data)