PUZZLE_INPUT_PATH = r"C:\Users\Max\Desktop\first_repo\first_repo\exercises\aoc_puzzle_input\\"


def find_floor_num(instructions):
    floor = 0
    for i in instructions:
        if i == "(":
            floor += 1
        elif i == ")":
            floor -= 1
        else:
            print("Only ') or '(' is allowed, hoe-hoe-hoe!")
    return floor


def belo_find_floor_room(instructions):
    """
    Lookup:
        - Ternary operator
        - Generators
        - Exceptions
    """
    return sum((1 if i == "(" else -1) for i in instructions)


def find_basement(instructions):
    floor = 0
    for i, instruction in enumerate(instructions):
    
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1
        else:
            print("Only ') or '(' is allowed, hoe-hoe-hoe!")

        if floor < 0: 
            return i + 1
    return 0



if __name__ == "__main__":
    with open(PUZZLE_INPUT_PATH + "2015_1", "r") as f:
        instructions = f.readline().strip()
        res = find_floor_num(instructions)
        print(res)
        print(find_basement(instructions))