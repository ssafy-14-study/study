T = int(input())
nums = []
for test_case in range(1, 1 + T):
    N = int(input())
    nums.append(N)

max_n = max(nums)

is_prime = [True] * (max_n + 1)
is_prime[0] = is_prime[1] = False
p = 2
while p * p <= max_n:
    if is_prime[p]:
        for k in range(p * p, max_n + 1, p):
            is_prime[k] = False
    p += 1

for N in nums:
    a = N // 2
    for x in range(a, 1, -1):
        if is_prime[x] and is_prime[N - x]:
            print(x, N - x)  # 작은 수 먼저 출력
            break