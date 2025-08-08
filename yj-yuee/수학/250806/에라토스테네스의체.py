N , K = map(int,input().split())
def find_prime(n, k):
    prime = [True]*(n+1)
    prime[0], prime[1] = False, False
    
    count = 0#지우지 않은 수중 가장 작은수를 찾는다 (2)
    for i in range(n+1):
        if prime[i] == True:
            for j in range(i, n+1, i):
                if prime[j] == False:#p지우고  p의배수크기를 순서대로 지움
                    continue
                prime[j] == [False]
                count+=1

                if count == k:
                    return j



print(find_prime(N, K))