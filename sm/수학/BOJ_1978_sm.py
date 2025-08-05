#소수 : 자신과 '1' 두가지 수만 약수로 가지는 수
N = int(input())
numbers = list(map(int, input().split()))

prime_count = 0

for num in numbers:
    if num != 1:
        cnt = 0
        for j in range(2,int((num**0.5)+1)):  #num을 그대로 사용하면 시간이 오래 걸림, 루트씌운값만 확인해도 충분
            if num % j == 0:
                cnt+=1 #약수의 갯수
        if cnt ==0: #약수가 없어야 소수
            prime_count += 1

print(prime_count)