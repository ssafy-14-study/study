import sys

# 소수 판별 (에라토스테네스의 체 사용)
MAX_N = 10000
is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX_N**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX_N + 1, i):
            is_prime[j] = False

# 입력 처리
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    
    # n//2부터 탐색 → 차이가 가장 작은 쌍부터 찾게 됨
    a = b = n // 2
    while a > 0:
        if is_prime[a] and is_prime[b]:
            print(a, b)
            break
        a -= 1
        b += 1