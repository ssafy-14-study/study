import sys
input = sys.stdin.readline
# 처음에 단순 input()으로 받았더니 시간초과가 떴었다.
N = int(input())
stack = []
for i in range(N):
    a = list(map(int,input().split()))
    if a[0] == 1:
        stack.append(a[1])
    elif a[0] == 2:
        if len(stack)>0:
            o = stack.pop()
            print(o)
        else:
            print(-1)
    elif a[0] == 3:
        print(len(stack))
    elif a[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 5:
        if len(stack)>0:
            print(stack[-1])
        else:
            print(-1)