import numpy as np

longString = "oh, well! it is just as he choose. Nobody wants him to come."

print( len(longString) )

count = 0
for ch in longString:
    count += 1
    #print(ch)
print(count, len(longString))

uniqueLetters = []
for letter in longString:
    if letter not in uniqueLetters:
        uniqueLetters.append(letter)
        print("unique letters = ", uniqueLetters)

uniqueLetters = []
letterSet = set()
for letter in longString:
     if letter not in uniqueLetters:
         uniqueLetters.append(letter)
         letterSet.add(letter)



print("unique letters  = ", len(uniqueLetters), uniqueLetters, )
print("unique set = ", len(letterSet), letterSet)

letterList = []
for elem in letterSet:
     letterList.append(letter)
     print("unique letters= ", uniqueLetters)