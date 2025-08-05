N, M = map(int, input().split())
A = []
for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)

B = []
for j in range(N):
    row = list(map(int, input().split()))
    B.append(row)

for z in range(N):
    C = []
    for x in range(M):
        row = A[z][x] + B[z][x]
        C.append(row)
    print(*C)