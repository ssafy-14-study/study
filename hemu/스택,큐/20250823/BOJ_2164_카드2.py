from collections import deque

N = int(input())

card = deque(range(1,N+1))

# 카드의 맨 위에서 빼고 그다음 위의걸 맨 아래로 보내기때문에 queue를 이용
# popleft()로 빼고 한번더 빼서 append
while len(card)>1:
    card.popleft()
    a = card.popleft()
    card.append(a)

b = card.popleft()
print(b)