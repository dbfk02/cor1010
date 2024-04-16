filename = "pg1342.txt"

filehandler = open(filename, "r", encoding='utf-8')

n = 0
ulist = []
while True:
    line = filehandler.readline()
    if not line:
        break 
    n += 1 
    for letter in line:
        if letter not in ulist:
            ulist.append(letter)

    #print(n,line)
    #if n > 10:
    #    break
#
print(n, len(ulist),ulist)


f2 = open("prog1.py", "r")
n = 0
while True:
    line = f2.readline()
    if not line:
        break 
    n += 1
    print(n,line)