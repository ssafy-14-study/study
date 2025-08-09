T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    max_cross = arr[0][0]
    for row in range(N):
        for col in range(N):
            cross_sum = arr[row][col]
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                for k in range(1,M):
                    new_row = row+(dr*k)
                    new_col = col+(dc*k)
                    if 0<=new_row<N and 0 <= new_col<N :
                        cross_sum += arr[new_row][new_col]
            if max_cross < cross_sum:
                max_cross = cross_sum

    
    max_diag = arr[0][0]
    for row in range(N):
        for col in range(N):
            diag_sum = arr[row][col]
            for dr, dc in [(1,-1),(1,1),(-1,1),(-1,-1)]:
                for k in range(1,M):
                    new_row = row + (dr*k)
                    new_col = col + (dc*k)
                    if 0 <= new_row <N and 0 <= new_col < N:
                        diag_sum += arr[new_row][new_col]
            if max_diag < diag_sum :
                max_diag = diag_sum


    if max_diag > max_cross :
        result = max_diag
    else:
        result = max_cross

    print(f'#{tc} {result}')