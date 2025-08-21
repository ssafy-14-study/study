T = int(input())
for case in range(T):
    N = int(input())
    zero = [1, 0]
    one = [0, 1]

    # N이 1 이하일 경우 바로 출력
    if N == 0 or N == 1:
        print(zero[N], one[N])
        continue

    # DP 계산 (필요한 N까지 채우기)
    for i in range(2, N+1):
        zero.append(zero[i-1] + zero[i-2])
        one.append(one[i-1] + one[i-2])

    print(zero[N], one[N])