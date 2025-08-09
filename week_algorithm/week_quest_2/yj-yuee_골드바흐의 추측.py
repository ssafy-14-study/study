T = int(input())
for ts in range(T):
    N = int(input())
    # N까지 소수 찾아서 True , False리스트 만들기
    prime = [True] * ( N + 1 )
    prime[0],prime[1] = False, False
    for i in range(2,int(N ** 0.5)+1):
        if prime[i]:
            for j in range(i*i,N+1,i):
                prime[j]=False

    # 리스트중에 합이 N이되는거 찾기(차이가 적은걸 찾으려면 N/2부터 탐색)
    for n1 in range(N//2,1,-1):
        if prime[n1]: #n1이 소수라면 계산
            n2 = N - n1
            if prime[n2]: #n2가 소수라면 출력 
                print(n1,n2) #중간값부터 줄여나가면서 탐색해서 n1이 항상 작거나 두수가 같음
                break
    
    # 처음 생각한대로 짠 코드 수정코드보다 비효율 적임
    '''
    prime = [True] * (N + 1)
    prime[0], prime[1] = False, False
    for i in range(2, int(N ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, N + 1, i):
                prime[j] = False

    prime_lst = [] #True, False 리스트가 있는데 소수리스트를 만들어 비교
    for k in range(N + 1):
        if prime[k]:
            prime_lst.append(k)
    min_ = 10000 
    num1, num2 = 0, 0
    for n1 in prime_lst:
        n2 = N - n1
            if prime[n2]:
                if ads(n1 - n2) < min_: #두수의 차의 절대값으로 비교함
                    min_ = abs(n1 - n2)
                    num1,num2 = n1, n2
    print(num1, num2)      
    '''
    