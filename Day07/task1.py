import os

beamChar = "|"
emptyChar = "."
laserChar = "S"
splitChar = "^"

for name in os.listdir("."):
    # only iterate through .txts
    if not name.endswith(".txt"):
        continue
    
    with open(name) as f:
        content = [list(line.rstrip("\n")) for line in f.readlines()]
        beamSplitCount = 0

        # iterate over lines and extend the laser beams
        for i in range(len(content) - 1):
            for j in range(len(content[i])):
                if content[i][j] == laserChar or content[i][j] == beamChar:
                    # check if beam has to be split or just passed down
                    if content[i + 1][j] == emptyChar:
                        content[i + 1][j] = beamChar
                    elif content[i + 1][j] == splitChar:
                        # increment split count
                        beamSplitCount += 1
                        content[i + 1][j - 1] = beamChar
                        content[i + 1][j + 1] = beamChar

        # print out file name and result
        print(f"file: {name} beam splits: {beamSplitCount}")