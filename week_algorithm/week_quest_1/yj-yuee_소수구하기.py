M, N = (map(int, input().split()))

prime = [True] * (N + 1) #
prime[0], prime[1] = False, False #0,1은 소수가 아니기때문에 제외

for i in range(2, int(N ** 0.5)+1):#범위는 N의 제곱근까지(약수의 대칭성)
    if prime[i]:
        for j in range(i*i, N+1, i):#i의 배수부터 N까지 i씩 제외
            prime[j]=False 

for k in range(M,N+1):
    if prime[k]: #if 문은 True라면 출력
        print(k) # 소수만 출력

