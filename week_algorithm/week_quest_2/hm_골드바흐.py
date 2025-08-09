# 시간 초과 ㅠㅠ 
# def find_primes(n):
#     if n<2:
#         return []
#     is_prime = [True]*(n+1)
#     is_prime[0] = is_prime[1] = False

#     for i in range(2, int(n**0.5)+1):
#         if is_prime[i]:
#             for j in range(i*i, n+1, i):
#                 is_prime[j] = False

#     primes  = [i for i in range(2,n+1) if is_prime[i]]
#     return primes

# T = int(input())
# for i in range(T):
#     N = int(input())
#     sosu = find_primes(N)
#     count = 0
#     for z in range(len(sosu)):
#         for q in range(len(sosu)-z):
#             if sosu[z] + sosu[z+q] == N:
#                 count += 1
#     print(count)

# 시간초과
# def find_primes(n):
#     if n<2:
#         return []
#     is_prime = [True]*(n+1)
#     is_prime[0] = is_prime[1] = False

#     for i in range(2, int(n**0.5)+1):
#         if is_prime[i]:
#             for j in range(i*i, n+1, i):
#                 is_prime[j] = False

#     primes  = [i for i in range(2,n+1) if is_prime[i]]
#     return primes

# T = int(input())
# for i in range(T):
#     N = int(input())
#     sosu = find_primes(N)
#     count = 0
#     for z in sosu:
#         if z> N//2:
#             break
#         if (N-z) in sosu:
#             count += 1

#     print(count)

#<정답> 메모리 40008KB 시간 600 ms
# def find_primes(n):
#     if n<2:
#         return []
#     is_prime = [True]*((n+1)//2)
#     is_prime[0] = False

#     for i in range(1, int(n**0.5)//2+1):
#         if is_prime[i]:
#             p = 2*i+1
#             for j in range(p*p, n+1, 2*p):
#                 is_prime[j//2] = False

#     primes = [2]
#     primes.extend(2*i+1 for i in range(1, len(is_prime)) if is_prime[i])
#     return primes

# MAX_N = 1000000
# all_prime = find_primes(MAX_N)
# sosu = set(all_prime)
# T = int(input())
# for i in range(T):
#     N = int(input())
#     count = 0
#     for z in all_prime:
#         if z> N//2:
#             break
#         if (N-z) in sosu:
#             count += 1

#     print(count)

# 이것도 맞음 메모리 43916, 시간 700 -> 결국 찾을때 list를 순회하는것보다 hash를 사용해 탐색하는 set이 빠르다는게 중요했었음
def find_primes(n):
    if n<2:
        return []
    is_prime = [True]*(n+1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    primes  = [i for i in range(2,n+1) if is_prime[i]]
    return primes

MAX_N = 1000000
all_prime = find_primes(MAX_N)
sosu = set(all_prime)
T = int(input())
for i in range(T):
    N = int(input())
    count = 0
    for z in all_prime:
        if z> N//2:
            break
        if (N-z) in sosu:
            count += 1
    print(count)