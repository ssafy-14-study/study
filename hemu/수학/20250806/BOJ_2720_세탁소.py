T = int(input())
for i in range(T):
    C = int(input())
    Q = 25
    D = 10
    N = 5
    P = 1
    Q_num = C//Q
    D_num = (C%Q)//D
    if (C%Q)%D >= 5:
        N_num= ((C%Q)%D)//N
        P_num = ((C%Q)%D)%N
    else:
        N_num = 0
        P_num = (C%Q)%D
    print(Q_num,D_num,N_num,P_num)