import numpy as np

arrayNumber = np.random.randint(0, 10, size=20)
print(arrayNumber)


uniqueList = []
for number in arrayNumber:
    if number in uniqueList:
        pass
    else:
        uniqueList.append(number)
#
print("unique: ", uniqueList)

uniqueList2 = list() #[]
for number in arrayNumber:
    if number in uniqueList:
        uniqueList2.append(number)
#
print("unique2: ", uniqueList2)

#uniqueList3 = [number for number in arrayNumber if number not in uniqueList]

myList = []
mylist2 = list()

# set, dict
uniqueSet = set()
for num in arrayNumber:
    uniqueSet.add(num)
#
print(uniqueSet)
for elem in uniqueSet:
    print(elem, end=' ')
print()

