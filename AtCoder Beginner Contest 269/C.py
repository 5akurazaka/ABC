from queue import Empty


N = int(input())

Nbinary = bin(N)[2:]

printList = ["0"]
cnt = 0
for keta in range(1, len(Nbinary) + 1):
    i = len(Nbinary) - keta
    if(Nbinary[i] == "1"):
        cnt += 1
        tempList = []
        for s in printList:
            if(len(s) != keta):
                temp = "1"+"0" * max(0, (keta - 1 - len(s)))
                temp = temp + s
                tempList.append(temp)
            else:
                tempList.append("1"+"0" * max(0, (keta - 1 - len(s))))
        printList += tempList
        if(cnt >= 15):
            break

for s in printList:
    print(int(s, 2))