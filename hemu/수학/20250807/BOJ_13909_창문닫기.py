# 메모리 초과 -> 배열을 사용하면 안되는 문제
# T = int(input())
# for e in range(T):
#     N = int(input())
#     window = [0]*N
#     for i in range(1,N+1):
#         for z in range(1,N+1):
#             if z%i == 0:
#                 if window[z-1]==0:
#                     window[z-1] = 1
#                 elif window[z-1]==1:
#                     window[z-1] = 0
#     count = 0
#     for j in window:
#         if j == 1:
#             count +=1
#     print(f"{e+1}번째 {count}")

# 창문 3개 -> 111-> 101 -> 100 
# 창문 4개 ->  1111 -> 1010 -> 1000 -> 1001 / 4반쩨 칭믄은 2와 4 두번 동작 -> 4의 약수(1,2,4) 열림 홀수개
# 창문 5개 -> 11111 -> 10101 -> 10001 -> 10011 -> 10010
# 창문 6개 -> 111111 -> 101010 -> 100011 -> 100111->100101 -> 100100 /6번째 창문은 2,3,6, 세번 동작 -> 6의 약수(1,2,3,6) 닫힘 짝수개
# 해당 창문의 약수가 홀수개이면 닫힘, 짝수개이면 열림. 홀수개의 약수를 갖는 수? -> 제곱수

# 시간 초과
# N = int(input())
# count = 0
# for i in range(1,N+1):
#     if i*i <= N:
#         count += 1
# print(count)
# for문으로 사용해서 시간이 초과한듯하다 -> while문을 사용해볼까?

N = int(input())
count = 0
i=1
while i*i <=N:
    count +=1
    i += 1

print(count)