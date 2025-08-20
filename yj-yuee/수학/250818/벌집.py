#육각형의 벌집
#1부터 시작해서 이웃하는 방에 1씩 증가하는 번호를 주소로 매길수있다
#규칙이 있을것같다 1번부터 가니까 거기까지 가는 층수를 세면 될거같은데
# 1번을 둘러싸고 6의 배수만큼 커짐
N = int(input())
layer = 1
cnt = 1
while N > cnt: #N까지 세기
    cnt += 6*layer 
    layer += 1

print(layer)