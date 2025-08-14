num = int(input())
M = 1000000000
abs_num = abs(num)  # 음수 입력도 양수로 변환해서 피보나치 계산
fib = [0] * (abs_num + 2)  # 인덱스 범위 안전하게 확보
fib[0] = 0
fib[1] = 1

# 피보나치 수열 계산 (절댓값 기준)
for i in range(2, abs_num + 1):
    fib[i] = (fib[i - 1] + fib[i - 2]) % M

# 결과 부호 결정
if num > 0:
    result_sign = 1
elif num < 0:
    result_sign = 1 if abs_num % 2 == 1 else -1  # 음수 피보나치 규칙 적용
else:
    result_sign = 0

print(result_sign)

# 피보나치 값 출력
if num != 0:
    print(fib[abs_num] % M)
else:
    print(0)