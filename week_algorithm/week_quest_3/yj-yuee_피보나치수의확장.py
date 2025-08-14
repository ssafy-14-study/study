#피보나치 수는 첫째항과 둘째항이 1,
#그다음부터는 바로 앞 두항의 합으로 이루어지는 수열
# F(0) = 0, F(1) = 1 일때 1이상의 n -> F(n) = F(n-1)+F(n-2)
#음수일때 피보나치 F(n-2) = F(n)-F(n-1) -> 절대값으로보면 같은 리스트
#양수가 현재항 찾기면 음수는 과거항 찾기 느낌
#기본 반복문 피보나치
'''
def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b, a+b
    return a
'''

# 음수 구분 피보나치
def fib(n):
    is_negative = n < 0 #음수인지 보자 (조건을 변수에 할당)
    abs_n = abs(n)

    n1, n2 = 0, 1
    for _ in range(abs_n):
        n1, n2 = n2 , n1+n2
    # 음수는 짝수일때 음수, 홀수일때는 양수
    if is_negative and abs_n % 2 == 0:
        return -n1
    else:
        return n1

N = int(input())
result = fib(N)

if result < 0:
    print(-1)
elif result == 0:
    print(0)
elif result > 0:
    print(1)

print(abs(result) % 1000000000) #1,000,000,000 이거넣어서 뭔 이상한 값나옴






