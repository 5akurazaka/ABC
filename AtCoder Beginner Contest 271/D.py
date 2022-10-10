N, S = map(int, input().split())
a = []
b = []
for i in range(N):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
#合計値：解のパターン
preSol = {0 : ""}
for i in range(N):
    nextSol = {}
    for preSum in preSol.keys():
        if(preSum + a[i] <= S):
            nextSol[preSum + a[i]] = preSol[preSum] + "H"
        if(preSum + b[i] <= S):
            nextSol[preSum + b[i]] = preSol[preSum] + "T"
    preSol = nextSol

if(S in preSol.keys()):
    print("Yes")
    print(preSol[S])
else:
    print("No")