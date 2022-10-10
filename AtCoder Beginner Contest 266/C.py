import numpy as np

A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))
C = np.array(list(map(int, input().split())))
D = np.array(list(map(int, input().split())))

vertexList = [A, B, C, D, A, B, C]

isConvex = True
for i in range(0, 4):
    a = vertexList[i]
    b = vertexList[i + 1]
    c = vertexList[i + 2]
    d = vertexList[i + 3]

    ab = np.array([b[0] - a[0], b[1] - a[1]])
    ad = np.array([d[0] - a[0], d[1] - a[1]])
    ac = np.array([c[0] - a[0], c[1] - a[1]])
    bd = np.array([d[0] - b[0], d[1] - b[1]])

    ac_ortho = np.array([ac[1], -ac[0]])

    if(np.dot(ac_ortho, bd) == 0):
         continue
    
    at = ab - bd * np.dot(ac_ortho, ab)/np.dot(ac_ortho, bd)

    if(np.linalg.norm(at) > np.linalg.norm(ac)):
        isConvex = False
        break

if(isConvex):
    print("Yes")
else:
    print("No")