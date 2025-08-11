N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
sum = [[0] * M for _ in range(N)] # 같은 크기의 행렬 생성
for i in range(N):
    for j in range(M):
        sum[i][j] = A[i][j] + B[i][j] # A와 B의 합을 생성한 행렬에 할당
        print(f'{sum[i][j]} ', end = '') # 같은 줄에 출력
    print() # 한 줄 띄어 출력 
