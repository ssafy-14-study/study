# T = int(input())
# for t_case in range(1, T+1):

#     N = int(input())
#     C = list(map(int, input().split()))

#     cnt = 1
#     cnt_list = []
#     for i in range(1, len(C)):
#         if C[i-1] < C[i]:
#             cnt +=1
#         else:
#             cnt_list.append(cnt)
#             cnt = 1

#     cnt_list.append(cnt)

#     print(f'#{t_case} {max(cnt_list)}')


#굳이 리스트를 사용하지 않고.. 더 간단하게.
T = int(input())
for t_case in range(1, T+1):

    N = int(input())
    C = list(map(int, input().split()))

    cnt = 1
    cnt_max = 1

    for i in range(1, N):
        if C[i-1] < C[i]:
            cnt += 1
        else:
            if cnt > cnt_max:
                cnt_max = cnt

            cnt =1
    if cnt > cnt_max:
        cnt_max = cnt

    print(f'#{t_case} {cnt_max}')