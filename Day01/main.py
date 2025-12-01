dial = 50
zero_count = 0

with open("input.txt") as f:
    l = [line.rstrip() for line in f]
    for line in l:
        if line.startswith("L"):
            dial -= int(line.lstrip("L"))
        elif line.startswith("R"):
            dial += int(line.lstrip("R"))

        dial = dial % 100
        if dial == 0:
            zero_count += 1
            print("0 count erhöht")
        print(dial)
    print(dial)
    print("password: " + str(zero_count))