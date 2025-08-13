T = int(input())
for case in range(1,T+1):
    N = int(input())
    arr = [list(input())for _ in range(N)]

    ans = 0
    delta = [[0,1],[1,0],[1,1],[-1,1]] #기준점이 왼쪽 위이기 때문에 우,하,우하,우상 만 해도 가능
    for i in range(N):
        for j in range(N):


            if arr[i][j] == 'o': # 좌표가 'o'일때만 찾아보기
                for di,dj in delta:
                    value = []
                    for c in range(1,5): #본인 좌표 제외
                        ni,nj = i+di*c, j+dj*c
                        if 0<=ni<N and 0<=nj<N:
                            value.append(arr[ni][nj])
                    # print(value),테스트용
                    if value.count('o') ==4:  #'o'가 4개라면 5개 연속
                        ans += 1
    if ans == 0:
        print(f'#{case} NO')
    else:
        print(f'#{case} YES')