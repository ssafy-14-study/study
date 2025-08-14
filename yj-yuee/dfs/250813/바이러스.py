#웜바이러스에 걸린 컴퓨터 찾기
#스택으로 풀거야
N = int(input()) # 컴퓨터의 수
M = int(input()) # 네트워크가 연결된 컴퓨터의 수 
c_arr = [[] for _ in range(N+1)]
for i in range(M):
    s_c, e_c = map(int, input().split())
    c_arr[s_c].append(e_c)
    c_arr[e_c].append(s_c) # 화사표가 없어서 양방향으로 잡음

def dfs(start_c):
    STACK = []
    visited = [False]*(N+1)
    STACK.append(start_c) #스택에 시작 컴퓨터 추가

    while STACK: #스택에 데이터가 있는동안
        a = STACK.pop()
        if not visited[a]: #없으면 
            visited[a] = True #들렸다는 표시로 True
        
        for b in c_arr[a]: # 배열의 a를 찾아가서 값가져오기
            if not visited[b]:
                STACK.append(b)
    return visited

result = dfs(1)
cnt = 0
for num in result: #True 인 값만 카운트
    if num :
        cnt +=1 # 1번 컴퓨터 값은 뺀다.
print(cnt-1)


    