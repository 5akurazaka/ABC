#修正済み
N = int(input())
coordinate = []
for i in range(N):
    coordinate.append(tuple(map(int, input().split())))


#周辺情報

def syuhenSet(x, y):
    return set([(x + 1, y), (x , y + 1), (x + 1, y + 1), (x - 1, y), (x, y - 1), (x - 1, y - 1)])

ans = {}
ans[0] = syuhenSet(coordinate[0][0], coordinate[0][1])
coordinate = coordinate[1:]

for cor in coordinate:
    inList = []
    for ansGroup in ans.keys():
        if(cor in ans[ansGroup]):
            inList.append(ansGroup)
    if(len(inList) == 0):
        ans[max(ans.keys()) + 1] = syuhenSet(cor[0], cor[1])
    else:
        unionSet = syuhenSet(cor[0], cor[1])
        for i in inList:
            unionSet = unionSet|ans.pop(i)
        ans[inList[0]] = unionSet

print(len(ans.keys()))