#N과 M이 있을때 길이가 M인 수열 구하기
#수열은 증가순으로 출력해야한다.
#백트래킹 -> 재귀함수

def dfs(n):
    if n == M:
        print(' '.join(map(str,lst))) #리스트 언패킹
        return

    for i in range(1,N+1):
        if not visited[i]:
            #사용했다고 기록후 리스트에 추가
            visited[i] = True
            lst.append(i)

            dfs(n+1)#다음번호
            #선택 취소 , 리스트에서 제거
            visited[i] = False
            lst.pop()

N,M = map(int, input().split())
lst = []
visited = [False] * (N + 1) #사용했는지 찾기

dfs(0)