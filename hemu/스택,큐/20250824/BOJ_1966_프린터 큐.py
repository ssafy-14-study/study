from collections import deque

T = int(input())
for tc in range(1,T+1):
    # n: 문서 개수, m: 궁금한 문서가 현재 큐의 몇번째인지
    N, M = map(int,input().split())
    I = deque(map(int,input().split()))

    print_count =0

    while True:
        # 작으면 뒤로
        if I[0]<max(I):
            a =I.popleft()
            I.append(a)

        else:
            I.popleft()
            print_count +=1
            # 뽑은게 원하던거면 반복 종료
            if M==0:
                break
        
        # 단계가 진행 될때마다 자리는 한칸 씩 앞으로 가는데  마이너스만 하면 -6,-7 처럼 계속 늘어나므로 길이로 나눈 나머지로 결정
        M = (M-1)%len(I)
    print(print_count)