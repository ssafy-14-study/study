import time
star_time = time.time()

[N, M] = list(map(int, input().split()))
for i in range(N, M + 1):
    num = 2
    remainder_list = []
    while num < i:
        remainder_list.append(i % num)
        num += 1

    if 0 in remainder_list:
        pass
    else:
        print(i)

end_time = time.time()
elapsed_time = end_time - star_time
print(f'코드 실행 시간 : {elapsed_time:.5f}초')


# 백준 시간 초과
# input을 sys.stdin.readline()으로 변경 후 실행
# 그래도 시간 초과

# 시간 측정 코드 추가
