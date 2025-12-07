import os
import re

for name in os.listdir("."):
    # only iterate through .txts
    if not name.endswith(".txt"):
        continue
    
    with open(name) as f:
        content = [line.rstrip("\n") for line in f.readlines()]
        
        numbers = content[:-1]
        operations = re.split("\\s+", content[-1])

        # filter out "" at end of ops
        if operations[-1] == "":
            operations = operations[:-1]
        
        # parse numbers
        nums4Calc = [[]]
        for i in range(max([len(x) for x in numbers])):
            s = ""
            for number in numbers:
                if i < len(number):
                    s += number[i]
            num = s.replace(" ", "")

            # if all are space -> start new list
            if num == "":
                nums4Calc.append([])
                continue

            # add number to last list in numbers
            nums4Calc[-1].append(num)

        overallsum = 0
        for i in range(len(nums4Calc)):
            overallsum += eval(operations[i].join(nums4Calc[i]))
            
        # calc the overall sum of sums and products
        print(f"file: {name}; sum = {overallsum}")