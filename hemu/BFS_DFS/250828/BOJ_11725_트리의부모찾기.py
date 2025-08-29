from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0]*(n+1)
visited = [False]*(n+1)

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
visited[1] = True

while queue:
    cur = queue.popleft()
    for near in graph[cur]:
        if not visited[near]:
            visited[near] = True
            parent[near] = cur
            queue.append(near)

for i in range(2,n+1):
    print(parent[i])