def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(2 ** 0.5)+1):
        if n % i == 0:
            return False
    return True

T = int(input())
for t in range(1, T+1):
    arr = []
    n = int(input())
    for i in range(2, n):
        if is_prime(i):
            arr.append(i)

    prime_list = []
    for j in range(len(arr)):
        for k in range(len(arr)):
            if n == arr[j]+arr[k]:
                prime_list.append((arr[j],arr[k]))

    if len(prime_list) == 1:
        print(*prime_list)

    min = 500000000
    if (len(prime_list) >= 2):
        for l in range(len(prime_list)):
            n1, n2 = prime_list[l]
            n3 == abs(n2-n1)
            if n3 < min :
                min = n3
                result1, result2 = prime_list[l]
        
        print(result1, result2)

