import math
from collections import deque
import time

N, M = map(int, input().split())


#start = time.perf_counter()

path = [[-1]*N for x in range(N)]
path[0][0] = 0

move = []
#縦横のみ
rootM = int(math.sqrt(M))

#syokika = time.perf_counter()

for i in range(rootM + 1):
    j = math.sqrt(M - i**2)
    if(int(j) == j):
        j = int(j)
        move.append((i, j))
        move.append((i, -j))
        move.append((-i, j))
        move.append((-i, -j))

#movement = time.perf_counter()

Now = deque()
Now.append((0, 0))
while Now:
    now = Now.popleft()

    for dxdy in move:
        nextX = now[0] + dxdy[0]
        nextY = now[1] + dxdy[1]
        if((0 <= nextX < N) & (0 <= nextY < N)):
            if(path[nextX][nextY] < 0):
                path[nextX][nextY] = path[now[0]][now[1]] + 1
                Now.append((nextX, nextY))


for x in path:
    print(*x)

""" print("初期化：" + str(syokika - start))
print("移動計算："+ str(movement - syokika))
print("完了：" + str(time.perf_counter() - movement)) """