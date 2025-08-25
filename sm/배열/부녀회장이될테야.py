T = int(input())

for _ in range(T):
    k = int(input())  # 층
    n = int(input())  # 호

 
    apt = [[0] * (n+1) for _ in range(k+1)]


    for i in range(1, n+1):
        apt[0][i] = i


    for floor in range(1, k+1):
        for room in range(1, n+1):
            apt[floor][room] = apt[floor][room-1] + apt[floor-1][room]

    print(apt[k][n])