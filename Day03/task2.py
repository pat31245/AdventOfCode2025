import os

for name in os.listdir("."):
    # only iterate through .txts
    if not name.endswith(".txt"):
        continue
    
    with open(name) as f:
        content = f.readlines()
        joltages = []
        # get highest joltage with magic
        for line in content:
            line = line.strip("\n")
            digits = []
            array = list(line)[:-12]
            # calc 12 digits
            for i in range(12):
                array.append(line[-12 + i])
                digits.append(max(array))
                # pop all values before the digit and the digit itself
                for j in range(array.index(digits[-1]) + 1):
                    array.pop(0)
            # add joltage to other joltage
            joltages.append(int("".join(digits)))

        # print out file name and sum of all joltages
        print(f"file: {name} joltage: {sum(joltages)}")
