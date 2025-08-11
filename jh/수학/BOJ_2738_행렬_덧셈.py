N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
sum = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        sum[i][j] = A[i][j] + B[i][j]
        print(f'{sum[i][j]} ', end = '')
    print()