#러시아 국기를 만들자....
T = int(input())
for ts in range(1,T+1):
    N,M = map(int, input().split())
    flags = [input() for _ in range(N)]
    cnt_lst = [[0]*3 for _ in range(N)]
    for c in range(N):
        row = flags[c] # 바꿔야 하는 수를 한줄씩 미리 세기로함
        cnt_lst[c][0] = M - row.count('W')
        cnt_lst[c][1] = M - row.count('B')
        cnt_lst[c][2] = M - row.count('R')

    min_cnt = N * M #가장큰값
    for i in range(N-2):#최소 두줄 남겨놓아야함 파랑 빨강
        for j in range(i+1,N-1):#i의다음줄 부터 최소 한줄 남겨놓아야함 빨강
            cnt_w = sum(cnt_lst[row1][0] for row1 in range(i+1))
            cnt_b = sum(cnt_lst[row2][1] for row2 in range(i+1,j+1))
            cnt_r = sum(cnt_lst[row3][2] for row3 in range(j+1,N))
            sum_color = cnt_w + cnt_b + cnt_r
            if min_cnt > sum_color:
                min_cnt = sum_color

    print(f'#{ts} {min_cnt}')