T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    dol_list = list(map(int,input().split()))
    for i in range(M):
        i,j = map(int,input().split())
        for a in range(j):
            if (i-2-a)>=0 and (i+a)<=N-1:
                if dol_list[i-2-a] == dol_list[i+a]: # 같을땐 뒤집기
                    if dol_list[i-2-a] == 0:
                        dol_list[i-2-a] = 1
                        dol_list[i+a] = 1
                    else:
                        dol_list[i-2-a] = 0
                        dol_list[i+a] = 0
                elif dol_list[i-2-a] != dol_list[i+a]: #다를땐 그냥 두기
                    pass
            elif (i-2-a)<0 and (i+a)>N-1: # 범위를 넘어가면 뒤집기 종료
                break
    print(f"#{tc}", *dol_list)