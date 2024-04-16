import numpy as np

print('my numpy version: ', np.__version__)

randomList = []
for i in range(1_000_000):
    n = np.random.randint(1, 20)
    randomList.append(n)
#
#print("randomList:", randomList)
    
randomArray = np.random.randint(1, 6, size=10000000)
print("randomArray: ", randomArray.shape, randomArray.size)

count = 1
count = 2
count = 3
count = 4
count = 5

for number in randomArray:
    if number == 1:
        count += 1
    elif number == 2:
        count += 1
    elif number == 3:
        count += 1
    elif number == 4:
        count += 1
    elif number == 5:
        count += 1

        #
print("the list contains ", count, "1s.")
print(f"the list contains {count} 2s.")
print("the list contains ", count, "3s.")
print("the list contains ", count, "4s.")
print("the list contains ", count, "5s.")
      
print("finishied.")