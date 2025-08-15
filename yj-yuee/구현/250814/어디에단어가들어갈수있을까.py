#예시를 보면 단어개수와 빈칸개수가 같아야 하는것 같음
T= int(input())
for t in range(1,T+1):
    N, K = map(int, input().split())
    voca_lst = [list(map(int, input().split())) for _ in range(N)]

    #가로 세로 상관없이 무조건 k인자리만 가능. 더 큰것도 안됨
    lst = []
    for i in range(N):
        r_cnt = 0 #가로 카운트 , 세로 카운트 만듬
        c_cnt = 0
        for j in range(N):
            #가로검사
            if voca_lst[i][j] == 1:
               r_cnt += 1
                #한번에 이어진 1의 개수를 구해야겠다
            elif voca_lst[i][j] == 0:
                #0을만나면 리스트에 추가 후 카운트 0
                lst.append(r_cnt)
                r_cnt = 0
            #세로검사
            if voca_lst[j][i] == 1:
                c_cnt += 1
            elif voca_lst[j][i]==0:
                lst.append(c_cnt)
                c_cnt = 0
        #1로 끝나는경우
        if r_cnt != 0:
            lst.append(r_cnt)
        if c_cnt != 0:
            lst.append(c_cnt)

    result = 0
    for k in lst:
        if k == K:
            result += 1

    print(f'#{t} {result}')