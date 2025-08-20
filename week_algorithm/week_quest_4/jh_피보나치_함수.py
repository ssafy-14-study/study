''' 풀 재귀 함수 - 시간 초과
def fibonacci(n):
    global cnt_0, cnt_1

    if n == 0:
        cnt_0 += 1
        return 0
    elif n == 1:
        cnt_1 += 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cnt_0 = 0
    cnt_1 = 0
    fibonacci(N)

    print(cnt_0, cnt_1)
'''
''' 재귀 함수_메모이제이션 - 상위 값이 메모리로 저장되기 때문에 호출 횟수를 구할 수 없음
def fibonacci_memo(n):
    global cnt_0, cnt_1, memo

    if n == 0:
        cnt_0 += 1
        return 0
    if n == 1:
        cnt_1 += 1
        return 1
    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

    return memo[n]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cnt_0 = 0
    cnt_1 = 0
    memo = {}
    fibonacci_memo(N)

    print(cnt_0, cnt_1)
'''
# 재귀 함수_DP(동적 계획) - 32412KB, 36ms
def fibonacci_DP(n):
    fibo = [0, 1]
    for i in range(2, n + 1):
        fibo.append(fibo[i - 1] + fibo[i - 2])

    return [fibo[n - 1], fibo[n]]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cnt_0 = 0
    cnt_1 = 0

    print(f"{' '.join(map(str, fibonacci_DP(N)))}")