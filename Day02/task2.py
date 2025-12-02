import os

# function to get every substing starting from index 0 to half of the word
def getSubstrings(inputString):
    subseqs = []
    for i in range((len(inputString) // 2) + 1):
        if len(inputString[:i]) > 0:
            subseqs.append(inputString[:i])
    return subseqs

# for testing so the example is displayed too
for name in os.listdir("."):
    # only iterate through .txts (i put the inputs in input.txt and example in example.txt)
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
            subseq_dict = getSubstrings(str(ID))
            IDisSubseqMultiplied = False

            # check for every subsequence if it can recreate the ID
            for subseq in subseq_dict:
                # check if subseq could possibly recreate ID and check if it reacreates
                if len(str(ID)) % len(subseq) != 0 and str(ID) == subseq * int(len(str(ID)) / len(subseq)):
                    invalidIds.append(ID)
                    break

        # print out name of the file and calculated password
        print(f"name: {name} with password: {sum(invalidIds)}")