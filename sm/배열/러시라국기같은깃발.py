T = int(input())
for case in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(input())for _ in range(N)]
    color = [{'W': 0, 'B': 0, 'R': 0}for _ in range(N)]

    # 각 케이스별 문자배열을 딕셔너리로 표현
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                color[i]['W'] +=1
            if arr[i][j] == 'B':
                color[i]['B'] +=1
            if arr[i][j] == 'R':
                color[i]['R'] +=1

    value = []
    for B_start in range(1,N-1):        # 파란색 줄의 시작줄의 범위
        for B_end in range(B_start,N-1):  # 파란색 줄의 끝줄의 범위
            cnt=0 # 바꿔야하는 색의 갯수

            for i in range(0,B_start): # White
                cnt += (color[i]['B'] + color[i]['R'])

            for i in range(B_start, B_end+1): # Blue
                cnt += (color[i]['W'] + color[i]['R'])

            for i in range(B_end+1, N): # Red
                cnt += (color[i]['W'] + color[i]['B'])

            value.append(cnt) #줄의 범위가 바뀔때마다 바꿔야하는 색의 갯수를 append

    ans = min(value)
    print(f'#{case} {ans}')





    ## 딕셔너리로 표현하기전

    # for B_start in range(1,N-1):
    #     for B_end in range(B_start,N):
    #         cnt=0

    #         for i in range(0,B_start-1):
    #             for j in range(M):
    #                 if arr[i][j] != 'W':
    #                     arr[i][j] = 'W'
    #                     cnt+=1
    #         for i in range(B_start, B_end):
    #             for j in range(M):
    #                 if arr[i][j] != 'B':
    #                     arr[i][j] = 'B'
    #                     cnt+=1
    #         for i in range(B_end+1, N):
    #             for j in range(M):
    #                 if arr[i][j] != 'R':
    #                     arr[i][j] = 'R'
    #                     cnt+=1
