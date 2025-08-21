# def fibonacci(n):
#     if n == 0:
#         print("0")
#         return 0
#     elif n == 1:
#         print("1")
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#N을 입력했을때 0과 1이 각각 몇번 출력 되는지
#O(N)

T = int(input())
for tc in range(T):
    N = int(input())
    #a는 0출력되는 횟수, b는 1이출력되는 횟수
    a, b = 1,0 #가장 초기값으로 만들어놓음
    for _ in range(N):
        next_a = b       # 새로운 0 횟수 = 이전의 1 횟수
        next_b = a + b   # 새로운 1 횟수 = 이전의 (0횟수+1횟수)
        a, b = next_a, next_b

    print(a,b)

# 간단한 패턴이 있음 0이 출력되는 횟수 f(n-1), 1이출력되는 횟수 f(n)