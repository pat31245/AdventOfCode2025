import os
import re
import math

for name in os.listdir("."):
    # only iterate through .txts
    if not name.endswith(".txt"):
        continue
    
    with open(name) as f:
        content = f.readlines()
        
        numbers = []
        operations = []
        
        # parse numbers/operations
        for line in content:
            splitLine = re.split(r"\s+", line.strip())
            # split mathematical operations from numbers
            if splitLine[0].isdigit():
                numbers.append(splitLine)
            else:
                operations = splitLine
                
        # calc the overall sum of sums and products
        sum = 0
        for i in range(len(numbers[0])):
            sum += eval(operations[i].join([numberList[i] for numberList in numbers]))
            
        print(f"file: {name}; sum = {sum}")