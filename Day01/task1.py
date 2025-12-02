dial = 50
zero_count = 0

with open("input_example.txt") as f:
    l = [line.rstrip() for line in f]
    for line in l:
        old_dial = dial
        if line.startswith("L"):
            dial -= int(line.lstrip("L"))
        elif line.startswith("R"):
            dial += int(line.lstrip("R"))

        if dial < 0:
            while dial < 0:
                dial += 100
        
        dial = dial % 100

        print(f"line {line}: {old_dial} -> {dial}")

        if dial == 0:
            zero_count += 1
            print("0 count erhöht")

    print("last dial state: " + str(dial))
    print("password: " + str(zero_count))