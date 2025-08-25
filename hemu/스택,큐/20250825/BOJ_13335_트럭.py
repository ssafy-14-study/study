from collections import deque

# n: 다리건너는 트럭개수. w: 다리길이 L은 최대하중
n,w,L = map(int,input().split())
truck = deque(map(int,input().split()))

dari = deque([0]*w)
time = 0

while dari:
    time += 1
    # 트럭이 다리를 지나는 과정
    dari.popleft()
    if truck:
        if sum(dari) + truck[0] <= L:
            dari.append(truck.popleft())
        else:
            dari.append(0)

print(time)