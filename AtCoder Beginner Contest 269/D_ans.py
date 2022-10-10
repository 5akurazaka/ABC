

N = int(input())
coordinate = []
for i in range(N):
    x, y = map(int, input().split())
    coordinate.append(tuple([x, y]))

visited = set()

from collections import deque
ans = 0
for i in range(N):
    cor  = coordinate[i]
    if(cor in visited):
        continue
    else:
        ans += 1
        visited.add(cor)
        next = deque()
        next.append(tuple(cor))

        while next:
            x, y = next.popleft()
            for s in set([(x + 1, y), (x, y + 1), (x + 1, y + 1), (x - 1, y), (x, y - 1), (x - 1, y - 1)]):
                if((not(s in visited)) & ((s[0], s[1]) in coordinate[i + 1 : N])):
                    next.append(s)
                    visited.add(s)

print(ans)

