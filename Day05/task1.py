import os

for name in os.listdir("."):
    # only iterate through .txts
    if not name.endswith(".txt"):
        continue
    
    with open(name) as f:
        content = f.readlines()
        
        freshRanges = []
        items = []
        parseRanges = True
        freshItems = 0
        
        # parse items and ranges of fresh items
        for line in content:
            if line.strip() == "":
                parseRanges = False
                continue
            # parse ranges
            if parseRanges:
                freshRanges.append(line.strip())
            # parse items
            else:
                items.append(int(line.strip()))
                
        # check how many items are fresh
        for item in items:
            for range in freshRanges:
                start, end = range.split("-")
                if item >= int(start) and item <= int(end):
                    freshItems += 1
                    break
                
        # print out file name and amount of rolls that can be picked up
        print(f"file: {name}; {freshItems} fresh items")