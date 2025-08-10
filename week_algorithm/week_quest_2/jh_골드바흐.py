def is_prime_number(input_n): # 주어진 짝수 n 보다 작은 소수 구하는 함수
    is_prime = []
    for i in range(input_n + 1):
        is_prime.append(True)

    n = 2
    while n * n <= input_n:
        if is_prime[n]:
            for i in range(n * n, input_n + 1, n):
                is_prime[i] = False
        n += 1
    
    prime_numbers = []
    for i in range(2, input_n + 1):
        if is_prime[i]:
            prime_numbers.append(i)
    
    return prime_numbers # n 보다 작은 소수들을 리스트로 반환
'''
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    prime_numbers = is_prime_number(n) # 변수에 n 보다 작은 소수 리스트 할당
    distance = 0 # 두 소수의 차이 저장
    new_distance = 0 # 새로운 두 소수의 차이 저장
    partition = [] # 파티션 리스트 생성
    for i in prime_numbers[]: # n 보다 작은 모든 소수를 순환
        for j in prime_numbers: # n 보다 작은 모든 소수를 순환
            if i + j == n: # 소수와 소수의 합이 n과 같다면
                new_distance = j - i # 두 소수의 차이를 변수에 할당
                if distance >= new_distance: # 방금 구한 두 소수의 차이를 기존의 소수의 차이와 비교
                    distance = new_distance # 새롭게 구한 두 소수의 차이가 기존 소수의 차이보다 작거나 같으면 기존 소수의 차이에 할당
                    partition.append(j)
                    partition.append(i) # partition 리스트에 두 소수 할당

    print(f'{partition[0]} {partition[1]}')
'''

'''
위와 같이 코드를 작성하여 제출을 했지만 시간 초과로 틀림
모든 prime_numbers의 값들을 순환할 필요는 없네
반만 순환해도 되네
'''

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    prime_numbers = is_prime_number(n) # 변수에 n 보다 작은 소수 리스트 할당
    distance = 0 # 두 소수의 차이 저장
    new_distance = 0 # 새로운 두 소수의 차이 저장
    partition = [] # 파티션 리스트 생성

    for i in prime_numbers[:(len(prime_numbers) // 2 + 3)]: # 처음부터 중간까지의 소수를 순환
        for j in prime_numbers[(len(prime_numbers) // 2 - 2):]: # 중간부터 끝까지의 소수를 순환
            if i + j == n: # 소수와 소수의 합이 n과 같다면
                new_distance = j - i # 두 소수의 차이를 변수에 할당
                if distance >= new_distance: # 방금 구한 두 소수의 차이를 기존의 소수의 차이와 비교
                    distance = new_distance # 새롭게 구한 두 소수의 차이가 기존 소수의 차이보다 작거나 같으면 기존 소수의 차이에 할당
                    partition = [j, i] # partition 리스트에 두 소수 할당

    print(f'{partition[0]} {partition[1]}')

'''
이렇게 하니 런타임 에러가 뜨네..
'''