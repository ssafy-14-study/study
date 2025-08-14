n = int(input())
mod_num = 1000000000
k = abs(n)  # 절댓값으로 양수 피보나치 계산
fibo = [0] * (k + 2)  # 인덱스 에러 방지
fibo[0] = 0
fibo[1] = 1
for i in range(2, k + 1):
    fibo[i] = (fibo[i - 1] + fibo[i - 2]) % mod_num

if n > 0: # n이 양수면 1
    sign = 1
elif n < 0: # n이 음수면
    if k % 2 == 1: # 절대값이 홀수일 때
        sign = 1 
    else: # 절대값이 양수일 때
        sign = -1
else:  # n이 0일 때
    sign = 0

print(sign)

if n != 0:
    print(fibo[k] % mod_num)
else:
    print(0)  
    