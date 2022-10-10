import sys
sys.setrecursionlimit(10 ** 6)

N, X, Y = map(int, input().split())

tree = [[] for x in range(N + 1)]
for i in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

def dfs(point, prepoint):
    if(point == Y):
        path.append(point)
        return True
    for s in tree[point]:
        if (s != prepoint):
            if(dfs(s, point)):
                path.append(point)
                return True
    return False


path = []
dfs(X, -1)
path.reverse()
print(" ".join(list(map(str, path))))