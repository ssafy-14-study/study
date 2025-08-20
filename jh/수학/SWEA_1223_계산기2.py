T = 10
for test_case in range(1, T + 1):
    length = int(input())
    N = input()
    stack = [0] * 1000
    top = -1
    icp = {'*' : 2, '+' : 1}
    isp = {'*' : 2, '+' : 1}
    postfix = ''
    for i in N:
        if i not in '*+':
            postfix += i
        else:
            if top == -1 or isp[stack[top]] < icp[i]:
                top += 1
                stack[top] = i
            elif isp[stack[top]] >= icp[i]:
                while top > -1 and isp[stack[top]] >= icp[i]:
                    postfix += stack[top]
                    top -= 1
                top += 1
                stack[top] = i
    for _ in range(length - len(postfix)):
        a = stack.pop(top)
        postfix += a
        top -= 1

    for i in postfix:
        if i not in '*+':
            top += 1
            stack[top] = int(i)
        else:
            a = stack[top]
            top -= 1
            b = stack[top]
            top -= 1
            if i == '*':
                top += 1
                stack[top] = a * b
            elif i == '+':
                top += 1
                stack[top] = a + b

    print(f'#{test_case} {stack[top]}')