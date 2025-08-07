M, N = map(int, input().split())

for num in range(M,N+1):
    cnt = 0
    if num == 1:
        continue
    for j in range(2, int(num**0.5)+1):
        if num % j == 0:
            cnt+=1
    if cnt ==0:
        print(num)
    


