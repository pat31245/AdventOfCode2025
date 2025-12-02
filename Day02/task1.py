import os

def getFirstSequence(inputString):
    return str(inputString[0:len(inputString) // 2])

for name in os.listdir("."):
    # only iterate through .txts
    if not name.endswith(".txt"):
        continue
    
    # open file, read contents
    with open(name) as f:
        content = f.readlines()
        # read only 1st line
        ranges = content[0].split(",")
        
        # get all ids
        invalidIds = []
        ids2check = []
        for r in ranges:
            for i in range(int(r.split("-")[0]), int(r.split("-")[1]) + 1):
                ids2check.append(i)
        
        # check ids for invalid ids
        for ID in ids2check:
            # filter the ones with odd length
            if len(str(ID)) % 2 == 1:
                continue

            if int(getFirstSequence(str(ID)) * 2) == ID:
                invalidIds.append(ID)

        # calc password
        password = 0
        for x in invalidIds:
            password += x

        # print out name of the file and password
        print(name)
        print(password)
        print("")