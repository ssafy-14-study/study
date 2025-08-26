# 북:0 동:1 남:2 서:3
def dir(d):
    d = d-1
    if d == -1:
        d= 3
    return d


N,M = map(int,input().split())
i,j,d = map(int, input().split())



room = [list(map(int,input().split()))for _ in range(N)]
cnt = 0

# 현재칸 청소
if room[i][j] == 0:
    room[i][j] = 2
    cnt += 1

d_r = [(-1, 0), (0, 1), (1, 0), (0, -1)]
while True:
    # 현재칸 청소
    if room[i][j] == 0:
        room[i][j] = 2
        cnt += 1

    cleaned = False

    for _ in range(4):
        d = dir(d)
        ni= i+d_r[d][0]
        nj= j+d_r[d][1]
        if 0<=ni<N and 0<=nj<M and room[ni][nj] == 0:
            i,j = ni,nj
            cleaned = True
            break

    if cleaned:
        continue

    back_d = (d+2)%4
    bi = i + d_r[back_d][0]
    bj = j + d_r[back_d][1]

    if 0 <= bi < N and 0 <= bj < M and room[bi][bj] != 1:
        i, j = bi, bj
    else:
        break  # 뒤가 벽이면 작동 종료

print(cnt)

    