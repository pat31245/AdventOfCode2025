import os

for name in os.listdir("."):
    # only iterate through .txts
    if not name.endswith(".txt"):
        continue
    
    with open(name) as f:
        content = f.readlines()

        joltage = 0
        # get highest joltage with magic
        for line in content:
            charArray = list(line.strip())
            firstDigit = max(charArray[:-1])
            secondDigit = max(charArray[charArray.index(firstDigit) + 1:])

            joltage += int(f"{firstDigit}{secondDigit}")

        # print out file name and sum of all joltages
        print(f"file: {name} joltage: {joltage}")