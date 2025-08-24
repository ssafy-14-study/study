# N,K = map(int,input().split())

# people = list(range(1,N+1))
# new_list = []

# while len(people)>0:
#     a = people.pop(K) # 생각해보니 이 경우는 K이하 남았을때 불가능
#     new_list.append(a)

# result = '<' + ','.join(map(str,new_list))+'>'
# print(result)

from collections import deque

N, K = map(int,input().split())

people = deque(range(1,N+1))
new_list = []

while len(people)>0:
    for i in range(K-1):
        a = people.popleft()
        people.append(a)
    b = people.popleft()
    new_list.append(b)

result = '<' + ', '.join(map(str,new_list))+'>'
print(result)