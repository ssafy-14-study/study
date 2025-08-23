import sys

N = int(input())
stack = []
for _ in range(1, N + 1):
    order = list(map(int, sys.stdin.readline().split()))
    if order[0] == 1:
        stack.append(order[1])
    elif order[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order[0] == 3:
        print(len(stack))
    elif order[0] == 4:
        if not stack:
            print(1)
        else:
            print(0)
    elif order[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)