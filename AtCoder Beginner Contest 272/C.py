N = int(input())
A = [x for x in map(int, input().split())]

even = []
odd = []
for a in A:
    if(a % 2 == 0):
        even.append(a)
    else:
        odd.append(a)

if((len(even) >= 2) | (len(odd) >= 2)):
    even.sort()
    odd.sort()

    if(len(even) < 2):
        print(odd[-1] + odd[-2])
    elif(len(odd) < 2):
        print(even[-1] + even[-2])
    else:
        evenSum = even[-1] + even[-2]
        oddSum = odd[-1] + odd[-2]
        print(max(evenSum, oddSum))
else:
    print(-1)