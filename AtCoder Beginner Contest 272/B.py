N, M = map(int, input().split())

kx = [[False for x in range(N)] for x in range(N)]
for x in range(N):
    kx[x][x] = True


for i in range(M):
    X = list(map(int, input().split()))[1:]
    for j in X:
        for k in X:
            kx[j -1][k-1] = True

flg = True
for l in kx:
    if(False in l):
        print("No")
        flg = False
        break
if(flg):
    print("Yes")