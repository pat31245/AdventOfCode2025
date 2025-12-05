import os

roll_field_char = "@"
empty_field_char = "."

def createField(fileContent: list[str]):
    field = []
    for line in fileContent:
        # append chars as list
        field.append([char for char in line.strip()])
    return field

def posValid(field: list[list[int]], x: int, y: int):
    return (x < len(field[0]) and y < len(field) and x >= 0 and y >= 0)

def adjacentRollsCount(field: list[list[str]], x: int, y: int):
    count = 0
    for x_offset in range(-1, 2, 1):
        for y_offset in range(-1, 2, 1):
            # filter out the field itself
            if x + x_offset == x and y + y_offset == y:
                continue
            if posValid(field, x + x_offset, y + y_offset):
                if field[y + y_offset][x + x_offset] == roll_field_char:
                    count += 1
    return count
    
for name in os.listdir("."):
    # only iterate through .txts
    if not name.endswith(".txt"):
        continue
    
    with open(name) as f:
        field = createField(f.readlines())
        rolls_removable = []
        
        while True:
            rolls_removable.append(0)
            # iterate over all lines and check for each paper roll if it can be picked up
            for y in range(len(field)):
                for x in range(len(field[0])):
                    if field[y][x] == roll_field_char:
                        if adjacentRollsCount(field, x, y) < 4:
                            rolls_removable[-1] += 1
                            field[y][x] = empty_field_char
            if rolls_removable[-1] == 0:
                break

        # print out file name and amount of rolls that can be picked up
        print(f"file: {name}; {sum(rolls_removable)} rolls can be picked up")