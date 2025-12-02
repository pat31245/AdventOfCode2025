with open("input.txt") as f:
    content = f.readlines()
    con = content[0].split(",")
    lengths = []
    for c in con:
        a, b = c.split("-")
        lengths.append(len(a))
        lengths.append(len(b))

    print(max(lengths))