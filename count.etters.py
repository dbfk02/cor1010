filename = "pg1342.txt"
unqLetters = set()

with open(filename, "r", encoding='utf-8') as filehandler:
    n = 0
    while True:
        line = filehandler.readline()
        if not line:
            break
        n += 1
        for letter in line:
            unqLetters.add(letter)
        #n += 1
        #print(n,line)
        #if n > 3:
        #    break
    #
#
print(f"Total {n} lines from {filename}: {len(unqLetters)} letters in the sat {unqLetters}")        

# 2. count each letter, going througt the txt file from the beginning


counts = {}
for lettre in unqLetters:
    counts[letter] = 0
print(counts)

with open (filename, "r", encoding='utf-8') as file:
    n = 0
    while True:
        line = file.readline()
        if not line:
            break
        n += 1

        for lettr in line:
            counts[letter] += 1
            print(ord(letter), counts[letter])

        if n == 1:
            print(line)
            break
#
        
print(counts)
#
for key, value in counts.items():
    if value > 0:
        print(ord(key), ":", value)
#