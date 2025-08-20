T = 10
for test_case in range(1, T + 1):
    length = int(input())
    N = input()
    postfix = N[0] + N[2:] + '+' # 연산자가 + 밖에 없어서 후위 표기식을 간단하게 구함
    stack = []
    for i in postfix:
        if i != '+': # 숫자가 나오면 stack에 append
            stack.append(int(i))
        else: # +가 나오면 stack에 앞에서부터 숫자를 꺼내 더해서 다시 앞에 넣음
            a = stack.pop(0) 
            b = stack.pop(0)
            stack.insert(0, a + b)

    print(f'#{test_case} {stack[0]}')