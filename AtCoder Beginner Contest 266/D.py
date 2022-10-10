N = int(input())
TXA = [tuple([0, 0, 0])]
for i in range(N):
    TXA.append(tuple(list(map(int, input().split()))))

#ある時刻、場所にいた時の最大の利得 DP[時刻index][場所]
DP = [{} for x in range(N + 1)]
DP[0] = {0 : 0}

for i in range(0, N):
    #現在地
    for x in DP[i]:
        t = TXA[i][0]
        a = DP[i][x]
    
        nextT = TXA[i + 1][0]

        #位置xから届く範囲の次のx
        for nextX in range(max(0, x - (nextT - t)), min(5, x + (nextT - t) + 1)):
            if(nextX == TXA[i + 1][1]):
                if(nextX in DP[i + 1].keys()):
                    DP[i + 1][nextX] = max(DP[i + 1][nextX], DP[i][x] + TXA[i + 1][2])
                else:
                    DP[i + 1][nextX] = DP[i][x] + TXA[i + 1][2]
            else:
                if(nextX in DP[i + 1].keys()):
                    DP[i + 1][nextX] = max(DP[i + 1][nextX], DP[i][x])
                else:
                    DP[i + 1][nextX] = DP[i][x]


ans = 0
for i in DP[N].keys():
    ans = max(ans, DP[N][i])

print(ans)

