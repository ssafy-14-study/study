# 바라보는 방향
# #d 0 -> [-1,0]북(위) 1-> [0,1]동(좌) 2 -> [1.0]남(하) 3-> [0,-1]서(우)

# 현재칸을 청소한다
# 청소되지않은 빈칸이 없다면
# 주변 4칸에 청소되지않은 빈칸이 있다면
# 들린것도 체크해야할거같은데 (청소체크)
# 그리고 반복하려면 while이 역시 편할거같음

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]  # 행 (북동남서)
dc = [0, 1, 0, -1]  # 열

# 청소한 칸의 수를 세는 변수
cnt = 0

while True:
    # 지금칸 확인 후 카운트
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1

    quest = False
    for i in range(4):
        d = (d + 3) % 4  # d를 인덱스로 활용
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            r, c = nr, nc
            quest = True  # 탐색 성공
            break  # 다시 rc로 가서 보기

    if not quest:  # 탐색이 여전히 False이라면
        # 한칸 후진하고 1번으로 돌아가기 -> d는 유지
        nr = r - dr[d]
        nc = c - dc[d]
        # 후진 했는데 벽이라면 끝
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 1:
            break
        else:
            r, c = nr, nc

print(cnt)
