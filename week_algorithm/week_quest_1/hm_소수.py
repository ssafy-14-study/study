
M, N = map(int,input().split())
# 시간 초과
# def is_prime_number(num):
#     num_prime = True
#     for i in range(2,num):
#         if num % i == 0:
#             num_prime = False
#     return num_prime

# for z in range(M, N+1):
#     x = is_prime_number(z)
#     if x == True:
#         print(z)

def is_prime_number(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

for z in range(M, N+1):
    x = is_prime_number(z)
    if x == True:
        print(z)