N, M,V = map(int,input().split())
G = [[] for _ in range(N+1)]
#---------양방향 추가------------
for _ in range(M):
    i,j = map(int,input().split())
    G[i].append(j)
    G[j].append(i)
# ------ 정점이 작은순서 부터-----------
for i in range(N+1):
    G[i].sort()

#---------DFS------------
stack =[V]
visited = []

while stack:
    need_visited = stack.pop() #뒤에서부터! 순서대로 따라갈거야! # 1 -> 2->4->3

    if need_visited not in visited: # 1 ->2->4->3
        visited.append(need_visited) #1 -> 2 ->4->3
        for i in reversed(G[need_visited]): # G[1] -> 234 ->432/14->41/ 123->321/14->41
            if i not in visited: # 1은 있네, 그럼 4 추가/ 1,2 다있네 3 추가!/4,1 다있어 추가 못해!
                stack.append(i) # stack이 0으로 종료!
print(*visited)
#---------BFS------------
queue = [V]
b_visited = []
while queue:
    current = queue.pop(0) # 앞에서부터 뽑아서! 가까운거부터 탐색해서 갈거야!

    if current not in b_visited:
        b_visited.append(current)
        for n in G[current]:
            if n not in b_visited and n not in queue:
                queue.append(n)
print(*b_visited)