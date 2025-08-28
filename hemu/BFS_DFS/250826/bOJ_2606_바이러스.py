N = int(input()) # 컴퓨터수
C = int(input()) # 연결된 쌍

graph = [[] for _ in range(N+1)]
com = [0]*(N+1)
for _ in range(C):
    a,b = map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]


def dfs(t):
    com[t]=1
    for x in graph[t]:
        if com[x] ==0:
            dfs(x)


dfs(1)
print(sum(com)-1)