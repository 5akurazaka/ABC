mojiretsu = input().split(" ")
N = int(mojiretsu[0])
Q = int(mojiretsu[1])

L = []
for i in range(N):
    L.append([int(x) for x in input().split(" ")])
S = []
for i in range(Q):
    S.append([int(x) for x in input().split(" ")])

for s in S:
    print(L[s[0] - 1][s[1]])