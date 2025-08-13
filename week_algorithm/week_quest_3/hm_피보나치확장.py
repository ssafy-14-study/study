# 런타임에러
# def fibo (n):
#     if n == 1 or n==0:
#         return n
#     elif n<0 or n>0:
#         return fibo(abs(n)-1) + fibo(abs(n)-2)

# F = int(input())
# if F>0 or abs(F)%2 == 1:
#     print(1)
#     print(fibo(F))
# elif F == 0:
#     print(0)
#     print(fibo(F))
# elif F<0 and abs(F)%2 ==0:
#     print(-1)
#     print(fibo(F))

# 런타임에러
# def fibo (n):
#     if n == 1 or n==0:
#         return n
#     elif n<0:
#         return fibo(abs(n)-1) + fibo(abs(n)-2) # -1이 들어갔을때 무한 루프 발생
#     elif n>=2:
#         return fibo(n-1) + fibo(n-2)

# F = int(input())
# if F>0 or abs(F)%2 == 1:
#     print(1)
#     print(fibo(F))
# elif F == 0:
#     print(0)
#     print(fibo(F))
# elif F<0 and abs(F)%2 ==0:
#     print(-1)
#     print(fibo(F))

# 런타임 에러 -> 아마 재귀 호출로 인해 큰수에서 스택오버플로우 있는듯..
# def fibo (n):
#     if n == 1 or n==0 or n == -1:
#         return abs(n)
#     elif n<-1:
#         return fibo(abs(n)-1) + fibo(abs(n)-2) 
#     elif n>=2:
#         return fibo(n-1) + fibo(n-2)

# F = int(input())
# if F>0 or abs(F)%2 == 1:
#     print(1)
#     print(fibo(F)%1000000000)
# elif F == 0:
#     print(0)
#     print(fibo(F)%1000000000)
# elif F<0 and abs(F)%2 ==0:
#     print(-1)
#     print(fibo(F)%1000000000) # 1000000000로 나눈 나머지로 해도 안됨 메모이제이션사용..?

# memo = {}
# def fibo (n):
#     if n in memo:
#         return memo[n]
#     if n == 1 or n==0 or n == -1:
#         result = abs(n)
#     elif n<-1 or n>=2:
#         result = fibo(abs(n)-1) + fibo(abs(n)-2)
#     memo[n] = result
#     return result


# F = int(input())
# if F>0 or abs(F)%2 == 1:
#     print(1)
#     print(fibo(F)%1000000000)
# elif F == 0:
#     print(0)
#     print(fibo(F)%1000000000)
# elif F<0 and abs(F)%2 ==0:
#     print(-1)
#     print(fibo(F)%1000000000) # 런타임 에러.. 반복문으로 다시하기


# memo = {}
# def fibo(n):
#     if n in memo:
#         return memo[n]
#     elif n==0 or n ==1 or n ==-1:
#         result= abs(n)
#     elif n>1:

#     elif n<-1 and abs(n)%2==0:

# memo = {}
# def fibo (n):
#     if n in memo:
#         return memo[n]
#     if n == 1 or n==0 or n == -1:
#         result = abs(n)
#     elif n<-1 or n>=2:
#         result = (fibo(abs(n)-1) + fibo(abs(n)-2))%1000000000
#     memo[n] = result
#     return result


# F = int(input())
# if F>0 or abs(F)%2 == 1:
#     print(1)
#     print(fibo(F))
# elif F == 0:
#     print(0)
#     print(fibo(F))
# elif F<0 and abs(F)%2 ==0:
#     print(-1)
#     print(fibo(F)) # 재귀는 안됨

F= int(input())
fibo = [0,1]
for i in range(2,abs(F)+1):
    fibo.append((fibo[i-1]+fibo[i-2])%1000000000)
if F%2 ==0 and F <0:
    print(-1)
    print(fibo[abs(F)])
elif F == 0:
    print(0)
    print(fibo[abs(F)])
else:
    print(1)
    print(fibo[abs(F)])