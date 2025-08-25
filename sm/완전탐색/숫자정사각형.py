def find_largest_square(N, M):
    K = min(N, M)
    for case in reversed(range(K)):
        for i in range(N - case):
            for j in range(M - case):
                if arr[i][j] == arr[i + case][j] and arr[i][j] == arr[i][j + case] and arr[i][j] == arr[i + case][j + case]:
                    return (case+1)**2
    return 0  # 조건을 만족하는 정사각형이 없을 경우




N,M = map(int,input().split())
arr = [list(map(int,input()))for _ in range(N)]

print(find_largest_square(N,M))
# found = False
# K = min(N,M)
# for case in reversed(range(K)):
#     for i in range(N-K+1):
#         for j in range(M-K+1):
#             if arr[i][j] == arr[i+case][j] and arr[i][j] == arr[i][j+case] and arr[i][j] == arr[i+case][j+case]:
#                 L = case
#                 found = True
#                 break
#         if found:
#             break
#     if found:
#         break

# 처음 if조건문을 만족하는 경우가 나오면 모든 for문을 종료하고 싶었는데 그런 문법은 없었고, 하나하나 break를 해서 빠져나와야하는 불편함
# 함수를 사용하여 return을 통해 조기 종료
