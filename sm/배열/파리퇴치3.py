T = int(input())
for case in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split()))for _ in range(N)]


    max_s = 0
    for i in range(N):
        for j in range(N):
            sum1 = arr[i][j]
            for di,dj in [[0,1],[-1,0],[0,-1],[1,0]]:
                for c in range(1,M):
                    ni,nj = i+di*c,j+dj*c
                    if 0<=ni<N and 0<=nj<N:
                        sum1 += arr[ni][nj]

            if max_s < sum1:
                max_s = sum1

            sum2 = arr[i][j]
            for dii,djj in [[1,1],[-1,1],[-1,-1],[1,-1]]:
                for c in range(1,M):
                    nii,njj = i+dii*c,j+djj*c
                    if 0<=nii<N and 0<=njj<N:
                        sum2 += arr[nii][njj]
            if max_s < sum2:
                max_s = sum2
    
    print(f'#{case} {max_s}')