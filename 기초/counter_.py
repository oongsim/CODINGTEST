from collections import Counter
# 등장 횟수를 세는 기능 제공

counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(counter['green'])
print(counter)
print(dict(counter)) # 사전 자료형으로 변환
