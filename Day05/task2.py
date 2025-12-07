import os

for name in os.listdir("."):
    # only iterate through .txts
    if not name.endswith(".txt"):
        continue
    
    with open(name) as f:
        content = f.readlines()
        
        ranges = []
        uniqueRanges = []
        freshIdCount = 0
        
        # parse ranges of fresh items
        for line in content:
            if line.strip() == "":
                break
            # parse ranges
            start, end = line.strip().split("-")
            ranges.append((int(start), int(end)))
                        
        ranges = sorted(ranges, key=lambda x: x[0] - x[1])
        
        # change ranges so no there are no overlapping values
        for r in ranges:
            if uniqueRanges == []:
                uniqueRanges.append(r)
                continue
            
            skipped = False
            for u in uniqueRanges:
                # check if range is already covered
                if r[0] >= u[0] and r[1] <= u[1]:
                    skipped = True
                    break
                
                # if start in any unique range, change it
                if r[0] >= u[0] and r[0] <= u[1]:
                    r = (u[1] + 1, r[1])
                    
                # if end in any unique range, change it
                if r[1] >= u[0] and r[1] <= u[1]:
                    r = (r[0], u[0] - 1)
                    
            # if file wasn't skipped add it to unique ranges
            if not skipped:
                uniqueRanges.append(r)
                
        for u in uniqueRanges:
            freshIdCount += u[1] - u[0] + 1
            
        # print out file name and amount of rolls that can be picked up
        print(f"file: {name}; {freshIdCount} ids are considered fresh")