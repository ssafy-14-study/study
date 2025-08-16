T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    stone = list(map(int, input().split()))
    for flip in range(1, M + 1): # 뒤집는 횟수만큼 for문 실행
        i, j = map(int, input().split())
        for k in range(1, j + 1): # 더하고 빼는 수는 1부터 시작
            if 0 <= (i - 1) - k < N and 0 <= (i - 1) + k < N: # 인덱스 수와 몇 번째 돌의 수는 1만큼 차이나기 때문에 i - 1을 기준으로
                if stone[(i - 1) - k] == stone[(i - 1) + k]: # i - 1 번째 돌을 기준으로 앞 뒤의 수 비교
                    if stone[(i - 1) - k] == 0: # 0으로 같으면
                        stone[(i - 1) - k] = 1 # 1로 뒤집는다
                        stone[(i - 1) + k] = 1
                    else: # 1로 같으면
                        stone[(i - 1) - k] = 0 # 0으로 뒤집는다
                        stone[(i - 1) + k] = 0

    print(f"#{test_case} {' '.join(map(str, stone))}") # 리스트의 값만 출력하기 위해 join 메소드 사용