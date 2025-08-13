N, M,V = map(int,input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    i,j = map(int,input().split())
    G[i].append(j)
    G[j].append(i)

for i in range(N+1):
    G[i].sort()
stack =[V]
visited = []

while stack:
    need_visited = stack.pop()

    if need_visited not in visited:
        visited.append(need_visited)
        for i in reversed(G[need_visited]):
            if i not in visited:
                stack.append(i)
print(*visited)

queue = [V]
b_visited = []
while queue:
    current = queue.pop(0)

    if current not in b_visited:
        b_visited.append(current)
        for n in G[current]:
            if n not in b_visited and n not in queue:
                queue.append(n)
print(*b_visited)