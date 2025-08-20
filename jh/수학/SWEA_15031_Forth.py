T = int(input())
for test_case in range(1, T + 1):
    N = list(input().split())
    stack = []
    try:
        for i in N:
            if i.isdigit(): # i가 숫자인 문자면 stack에 int로 형변환 후 append
                stack.append(int(i))
            elif i in '+-*/': # i가 연산자면
                a = stack.pop() # stack에서 숫자 pop
                b = stack.pop() # pop 순서 중요!
                if i == '+':
                    stack.append(b + a)
                if i == '-':
                    stack.append(b - a) # 뺄셈 순서 중요!
                if i == '*':
                    stack.append(b * a)
                if i == '/':
                    stack.append(b // a) # 나눗셈 순서 중요!
            elif i == '.': # i가 .이면 for문 종료
                break
        if len(stack) == 1 and str(stack[0]).isdigit(): # stack에 숫자 하나 남았는지 확인
            print(f'#{test_case} {stack[0]}')
        else:
            print(f'#{test_case} error') # 아니면 error 출력
    except :
        print(f'#{test_case} error') # 연산 도중 error 나면 except문으로 error 출력