
#함수 정의 하지 않고 쭈욱..

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int,input().split())) for _ in range(N)]

#     fly_max_kill = 0
#     for row in range(N-M+1):              #범위 설정
#         for col in range(N-M+1):
#             fly_sum =0
#             for i in range(row, row+M):           #크기 M만큼만 구하기
#                 for j in range(col, col+M):
#                     fly_sum += arr[i][j]
#             if fly_sum > fly_max_kill :
#                 fly_max_kill = fly_sum

#     print(f'{tc} {fly_max_kill}')
            

#함수 정의하고
def fly_kill_sum(row, col, M):
    kill_sum = 0
    for i in range(row,row+M):
        for j in range(col,col+M):
            kill_sum += arr[i][j]

    return kill_sum



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_sum = 0
    for row in range(N-M+1):
        for col in range(N-M+1):
            kill_sum = fly_kill_sum(row, col, M)
            if max_sum < kill_sum :
                max_sum = kill_sum
    print(f'#{tc} {max_sum}')

