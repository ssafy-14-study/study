# 에라토스테네스의 체
def prime_list(num):
    prime = [True] * (num + 1)
    prime[0], prime[1] = False, False
    for i in range(2, int(num ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, num + 1, i):
                prime[j] = False
    return [i for i in range(2, num + 1) if prime[i]]


primes = prime_list(10000)
prime_set = set(primes)  

T = int(input())

for t in range(T):
    n = int(input())
    
    diff = 10001
    result1, result2 = 0, 0
    
    for i in range(len(primes)):
        prime_num = n - primes[i]
        if prime_num in prime_set:  
            if abs(prime_num - primes[i]) < diff:
                diff = abs(prime_num - primes[i])
                result1, result2 = primes[i], prime_num

    print(result1, result2)


