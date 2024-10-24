inList = [44, 55, 5, 22, 333, 4, 5, 112345]

def insertionSort(inList):
    outList = []
    for i in range(0, len(inList) - 1):
        if inList[i] > inList[i + 1]:
            outList.append(inList[i + 1])
            print(inList[i + 1])
        else:
            outList.append(inList[i])
    return outList

print(insertionSort(inList))