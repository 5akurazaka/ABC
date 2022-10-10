from math import inf

N, M = map(int, input().split())
A = list(map(int, input().split()))

#key : index と 部分集合の累積数
DP = {(0, 1) : A[0]}
for i in range(1, N - M + 1):
    DP[(i, 1)] = max(DP[(i - 1, 1)], A[i])

maxSol = -inf
for usedI in range(1, M):
    DP[(usedI, usedI + 1)] = DP[(usedI - 1, usedI)] + A[usedI]* (usedI + 1)
    for index in range(usedI + 1, N - (M - usedI) + 1):
        DP[(index, usedI + 1)] = max(DP[(index - 1, usedI)] + A[index]* (usedI + 1), DP[(index - 1, usedI + 1)])
        
        if(usedI + 1 == M):
            maxSol = max(maxSol, DP[(index, usedI + 1)])

print(maxSol)
