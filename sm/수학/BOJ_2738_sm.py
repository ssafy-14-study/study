rows, cols = map(int, input().split())

matrix_A = []


for i in range(rows):
    lst_A = list(map(int, input().split()))
    matrix_A.append(lst_A)


matrix_B = []

for i in range(rows):
    lst_B  = list(map(int,input().split()))
    matrix_B.append(lst_B)


for i in range(rows):
    for j in range(cols):
        print(matrix_A[i][j] + matrix_B[i][j],end=" ") 
    print()