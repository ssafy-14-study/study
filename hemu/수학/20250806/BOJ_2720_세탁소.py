T = int(input())
for i in range(T):
    C = int(input())
    #정수로 거스름돈을 받아오므로 quarter등도 정수로 처리
    Q = 25
    D = 10
    N = 5
    P = 1
    # 제일 큰 단위의 몫은 단위를 남겨줘야할 갯수 나머지는 다음 단위들이 같은 것 반복
    Q_num = C//Q
    D_num = (C%Q)//D
    if (C%Q)%D >= 5:
        N_num= ((C%Q)%D)//N
        P_num = ((C%Q)%D)%N
    else:
        N_num = 0
        P_num = (C%Q)%D
    print(Q_num,D_num,N_num,P_num)