T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(input())
    cnt = 0
    idx = 0
    cur_max = 0
    while idx < N:
        if arr[idx] == '1':
            cnt += 1
            idx += 1
            if cur_max < cnt:
                cur_max = cnt
        else:
            cnt = 0
            idx += 1

    print(f'#{test_case} {cur_max}')