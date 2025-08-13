T = int(input())
for ts in range(T):
    N = int(input())

    def compare(p_lst, e_lst):
        for i in range(len(p_lst)) :
            if p_lst[i] != e_lst[i]: #두개가 다르면 여기가 시작 인덱스
                start = i
                return True, start
        return 0,0

    def reverse(n, p_lst):
        for j in range(N - 1, n - 1, -1):# 뒤부터 바뀐인덱스까지 0,1바꾸기
            p_lst[j] = 1 - p_lst[j]
        return p_lst


    pre_switches = list(map(int, input().split()))
    end_switches = list(map(int, input().split()))
    cnt = 0
    #두개가 다를동안 반복
    while pre_switches != end_switches:
        #다른 첫지점을 찾는다 여기가 뒤집을 위치
        check, start_idx = compare(pre_switches,end_switches)
        #그다음 부터는 바뀐리스트랑 비교해야함 바꾸고 카운트 +1
        reverse(start_idx, pre_switches)#파이썬의 특징 때문에 재재정은 하지않음
        cnt += 1

    # end랑 같아졌다면 끝 내고 cnt값 출력
    print(f'#{ts+1} {cnt}')
