import math
import itertools
import bisect

N, M = map(int, input().split())
S = []
T = []
for i in range(N):
    S.append(input())
for i in range(M):
    T.append(input())

T.sort()




def isInT(x, T):
    index = bisect.bisect(T,x)

    if(index > 0):
        return x == T[index - 1]
    else:
        return False

def dfs(x, S_dash, usedIndex, maxHyphen, usedHyphen):
    if(usedIndex == N - 1):
        if(isInT(x, T) | (len(x) > 16) | (len(x) < 3)):
            return False
        else:
            print(x)
            return True
    stack = [S_dash[usedIndex + 1]] + ["_" * (i + 1) for i in range(maxHyphen - usedHyphen)]
    for i in range(len(stack)):
        ret = False
        sol = ""
        if(i == 0):
            sol = x + "_" + stack[i]
            ret = dfs(sol, S_dash, usedIndex + 1, maxHyphen, usedHyphen)
        else:
            sol = x + stack[i]
            ret = dfs(sol, S_dash, usedIndex, maxHyphen, usedHyphen + i)
        if(ret):
            return True

minimumJoin = len("_".join(S))
maxHyphen = 0
if(len(S) > 1):
    maxHyphen = max(0, 16 - minimumJoin)

findFlg = False
for s_dash in itertools.permutations(S):
    x = s_dash[0]
    if(dfs(x, s_dash, 0, maxHyphen, 0)):
        findFlg = True
        break

if(not(findFlg)):
    print(-1)
