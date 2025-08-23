#승환이의 간식먹기
#대기라인을 스택으로 사용해서 현재 차례인지 찾으면 될듯
#근데 N이 왜필요한지 모르겠음
N = int(input())
line = list(map(int, input().split()))
STACK = []
num = 1

current = 0
while current < len(line):
        #현재줄의 순번 확인
        if line[current] == num:
            num+=1 #다음대기번호
            current+=1 #다음 학생

        #대기공간 확인
        elif STACK and STACK[-1] == num:#스택이 비어있지않고 스택의 마지막이 대기번호와 일치한다면
            STACK.pop()
            num +=1

        else:
            STACK.append(line[current])
            current+=1

while STACK: #대기공간확인
    if STACK[-1] == num: # 스택의 마지막이 현재 대기번호와 맞는지
        STACK.pop()
        num+=1
    else:
        break

if not STACK:
    print("Nice")
else:
    print("Sad")