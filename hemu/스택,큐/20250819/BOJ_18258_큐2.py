from collections import deque
import sys
input = sys.stdin.readline
# 처음에 stack 처럼 리스트로 만들고 pop(0) 했더니 O(n)의 시간복잡도를 가져 시간초과가 남
# deque를 이용해 popleft()를 사용하면 O(1)의 시간복잡도를 가짐 -> 통과
# 큐 : 선입 선출
queue = deque()
N = int(input())
for i in range(N):
    a = list(input().split())
    if a[0] == 'push':
        queue.append(int(a[1]))
    elif a[0] == 'pop':
        if len(queue)>0:
            b = queue.popleft()
            print(b)
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(queue))
    elif a[0] == 'empty':
        if len(queue) >0:
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        if len(queue)>0:
            print(queue[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if len(queue)>0:
            print(queue[-1])
        else:
            print(-1)

# 파일올리기