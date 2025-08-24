# N,M = map(int,input().split())
# r,c,d = map(int,input().split()) # 0:북 1:동 2:남 3:서
# clean = [list(map(int,input().split())) for _ in range(N)]

# def clean_dir(clean,d,N,M,x,y):
#     if d ==0:
#         if 0<=clean[x][y-1]<M:
#             x = x
#             y = y-1
#             d = 3
#     elif d ==1:
#         if 0<=clean[x-1][y]<N:
#             x=x-1
#             y=y
#             d = 0
#     elif d ==2:
#         if 0<=clean[x][y+1]<M:
#             x = x
#             y = y+1
#             d = 1
#     elif d ==3:
#         if 0 <=clean[x+1][y]:
#             x = x+1
#             y = y
#             d = 2
#     return x,y,d

# count = 0
# while True:
#     if clean[r][c] ==0:
#         clean[r][c] =2
#         count +=1

#     for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
#         nx,ny = r+dx,c+dy
#         if 0<=nx<N and 0<=ny<M and clean[nx][ny] ==0:    
#             x,y,d = clean_dir(clean,d,N,M,nx,ny)
#             if clean[x][y] == 0:
#                 clean[x][y] = 2
#                 r = x
#                 c = y
#                 count +=1
#                 break
#     else:
#         if d == 0:
#             r = r-1
#             c =c
#         elif d ==1:
#             r = r
#             c = c-1
#         elif d ==2:
#             r= r+1
#             c = c
#         elif d ==3:
#             r = r
#             c = c+1
        
#         if clean[r][c] ==1:
#             break
#         else:
#             continue
# print(count)

N,M = map(int,input().split())
r,c,d = map(int,input().split()) # 0:북 1:동 2:남 3:서
clean = [list(map(int,input().split())) for _ in range(N)]

# d의 방향만 정하기
def clean_dir(d):
    if d ==0:
        d = 3
    elif d ==1:
        d = 0
    elif d ==2:
        d = 1
    elif d ==3:
        d = 2
    return d

count = 0
if clean[r][c] ==0:
    clean[r][c] =2
    count +=1
while True:
    cleaned = False
    # 네번을 돌았을때 없으면 1번경우 돌다가 있으면 반복문 정지
    for _ in range(4):
        d = clean_dir(d)
        if d == 0:
            nx = r-1
            ny =c
        elif d ==1:
            nx = r
            ny = c+1
        elif d ==2:
            nx= r+1
            ny = c
        elif d ==3:
            nx = r
            ny = c-1

        if 0<=nx<N and 0<=ny<M and clean[nx][ny] ==0:
            clean[nx][ny] =2
            r,c = nx,ny
            count +=1
            cleaned = True
            break

    if not cleaned:
        if d ==0:
             r = r+1
        elif d ==1:
            c = c-1
        elif d ==2:
            r = r-1
        elif d ==3:
            c = c+1
        if clean[r][c] ==1:
            break

print(count)
