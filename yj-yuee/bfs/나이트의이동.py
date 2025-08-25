from collections import deque
#나이트가 몇번 움직이면 이 칸으로 이동할까?
#나이트가 한번에 이동할수있는 거리를 보면 
dx = [+2, +1, -1, -2, -2, -1, +1, +2]
dy = [+1, +2, +2, +1, -1, -2, -2, -1]

def bfs(si,sj,gi,gj):
    Q.append((si,sj))
    visited[si][sj] = 1 #시작위치는 1로 변경

    while Q:
        ti, tj = Q.popleft()
        if ti == gi and tj == gj:
            print(visited[ti][tj]-1)#도착위치가 미로랑 다른점 : 이동 횟수인지 중간 개수인지
            return True
        for i in range(8):
            nr = ti + dx[i]
            nc = tj + dy[i]
            if 0<=nr < N and 0<= nc < N and visited[nr][nc]==0:
                visited[nr][nc] = visited[ti][tj]+1
                Q.append((nr,nc))


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    s1, s2 = map(int,input().split())#나이트의 시작위치
    g1, g2 = map(int,input().split())#나이트가 도착할 위치
    visited = [[0]* N for _ in range(N)]
    
    Q = deque()

    bfs(s1,s2,g1,g2)
