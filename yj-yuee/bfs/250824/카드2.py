from collections import deque
#N장의 카드
#제일 위에 있는 카드를 버린다. 그다음 제일 위에있는 카드를 제일 아래있는 카드 밑으로 옮긴다.
#카드가 한장이 남을때 까지 반봅
def card(N):
    arr = deque(range(1, N+1))

    while len(arr) > 1:
        arr.popleft()#첫번쩨를 버리고
        next_n = arr.popleft() #그다음 카드를 맨뒤로 넣는다
        arr.append(next_n)
    print(arr[0])

card(int(input()))

#시간 124ms

'''
#시간초과
def card(N):
    arr = [i for i in range(1,N+1)]
    while len(arr) != 1:
        arr.pop(0)#첫번쩨를 버리고
        next_n = arr.pop(0)
        arr.append(next_n)
    print(arr[0])


card(int(input()))

'''