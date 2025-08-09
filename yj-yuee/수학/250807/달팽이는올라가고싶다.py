A, B, V = map(int, input().split())

# dalpang = 0
# day= 0
# while dalpang < V:
#     day += 1
#     dalpang += A
#     if dalpang < V:
#         dalpang -= B #단순하게 접근했더니 나무 높이가 높을때 시간초과남

day = (V-A) // (A-B) #마지막날을 빼고 올라가는 날짜

if (V-A) % (A-B) > 0:#나누어 떨어지지 않으면 마지막 전날이 아님 전전날임
    day += 1

print(day+1)