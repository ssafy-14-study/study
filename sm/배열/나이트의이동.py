# 나이트의 이동
def BFS(si,sj):
    Q = [[si,sj]]
    visited = [[0]*l for _ in range(l)]

    while Q:
        x,y = Q.pop(0)
        if x == ei and y == ej:
            return visited[x][y]
        
        for di,dj in [[1,2],[1,-2],[2,1],[2,-1],[-1,2],[-1,-2],[-2,1],[-2,-1]]:     # delta설정
            ni,nj = x+di,y+dj
            if 0<=ni<l and 0<=nj<l and visited[ni][nj] == 0:
                Q.append([ni,nj])
                visited[ni][nj] = visited[x][y] + 1     #몇번이동하였는지 세주기
    return 0



T = int(input())
for case in range(T):
    l = int(input())
    si,sj = map(int,input().split())    #시작점
    ei,ej = map(int,input().split())    #끝점

    # chess = [[0]*l for _ in range(l)]     #체스판도 따로 리스트로 만들어서 사용할줄 알았는데 사용x
    ans = BFS(si,sj)
    print(ans)