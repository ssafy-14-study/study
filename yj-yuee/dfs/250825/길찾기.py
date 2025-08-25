def dfs():
    STACK = []
    STACK.append(0)
    visited = [False] * 101
    while STACK:

        v = STACK.pop()

        if not visited[v]:
            visited[v] = True

            if v == 99:
                return 1

            for w in graph[v]:
                if not visited[w]:
                    STACK.append(w)
    return 0


for tc in range(10):
    T, N = map(int, input().split())
    data = list(map(int, input().split()))

    graph = [[] for _ in range(101)]
    for i in range(0,N*2,2):
        s_n = data[i]
        e_n = data[i+1]
        graph[s_n].append(e_n) #단방향


    # for i in range(101): #노드 확인하기
    #     if graph[i]:
    #         print(f'{i}번 노드 -> {graph[i]}')
    print(f'#{T} {dfs()}')



