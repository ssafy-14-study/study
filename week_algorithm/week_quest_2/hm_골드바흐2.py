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

MAX_N = 10000
all_prime = find_primes(MAX_N)
sosu = set(all_prime)
T = int(input())
for i in range(T):
    N = int(input())
    for z in range(N//2,1,-1):
        #a<=b and a+n=N일때 N//2에 가까울수록 절댓값 a-b가 작음
        if z in sosu and (N-z) in sosu:
            print(z,N-z)
            break