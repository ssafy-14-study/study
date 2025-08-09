N, K = map(int, input().split())
# K는 계산해야할 총합, N개의 줄에 동전의 가치 Ai가 오름차순으로 주어짐
coins = []
for _ in range(N):
    coins.append(int(input()))

count = 0
# 오름 차순 정렬이므로 역순 -> 큰수부터
for i in range(N-1, -1, -1):
    coin = coins[i]
    # 돈을 큰 동전으로 나눈 몫이 동전의 개수
    num_coins = K // coin
    count += num_coins
    # 돈에서 동전*개수 만큼 빼준걸 대입 다음 연산에 이용
    K -= num_coins*coin

    if K==0:
        break
print(count)