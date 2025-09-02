import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = []

for _ in range(N):
    cmd = input().split()
    
    if cmd[0] == '1':  # push
        stack.append(int(cmd[1]))
    elif cmd[0] == '2':  # pop
        if stack:
            result.append(str(stack.pop()))
        else:
            result.append("-1")
    elif cmd[0] == '3':
        result.append(str(len(stack)))
    elif cmd[0] == '4':
        result.append("1" if not stack else "0")
    elif cmd[0] == '5':
        if stack:
            result.append(str(stack[-1]))
        else:
            result.append("-1")


print("\n".join(result))
