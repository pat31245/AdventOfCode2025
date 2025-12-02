import os

def printDebug(s):
    print(s)
    pass

for name in os.listdir("."):
    # skip .py and output files
    if not name.endswith(".txt"):
        continue

    with open(name) as f:
        dial = 50
        zero_count = 0
        output = []

        l = [line.rstrip() for line in f]
        currentLine = 0
        # for every line rotate dial
        for line in l:
            old_dial = dial

            # check whether dial must be incremented / decremented
            remove = False
            diff = 0
            if line.startswith("L"):
                diff = int(line.lstrip("L"))
                remove = True
            elif line.startswith("R"):
                diff = int(line.lstrip("R"))
                remove = False

            # increment / decrement dial 1 by 1 (other method didnt work for some reason)
            dial_passed_zero = 0
            if remove:
                for i in range(diff):
                    dial -= 1
                    if dial == -1:
                        dial += 100

                    if dial == 0:
                        zero_count += 1
                        dial_passed_zero += 1
            else:
                for i in range(diff):
                    dial += 1
                    if dial == 100:
                        dial -= 100

                    if dial == 0:
                        zero_count += 1
                        dial_passed_zero += 1

        # print out name of file, last dial state and password
        print(f"file: {name} last dial state:  {str(dial)} password: {str(zero_count)}")