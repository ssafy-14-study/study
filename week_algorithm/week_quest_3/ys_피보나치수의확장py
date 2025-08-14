def fibo(n):
    if 0 <= n < 2 :
        return n
    elif n >= 2 :
        return fibo(n-1)+fibo(n-2)
    else:

        # return fibo(n) * ((-1) **(n+1))   #-> maximum recursion depth exceeded 오류,,,,,
        sign = -1 if abs(n) % 2 == 0 else 1     #짝수면 부호가 -1, 홀수면 1
        return sign * fibo(-n)
    
def fibo_print(n):
    if fibo(n) > 0 :
        print(1)
    elif fibo(n) == 0 :
        print(0)
    else: print(-1)


n = int(input())
fibo_print(n)
result = abs(fibo(n))%1000000000
print(result)

#런타임 에러............