PUZZLE_INPUT_PATH = "/home/a.belo/personal/STAS/first_repo/exercises/aoc_puzzle_input/"


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


if __name__ == "__main__":
    with open(PUZZLE_INPUT_PATH + "2015_1", "r") as f:
        instructions = f.readline().strip()
        res = find_floor_num(instructions)
        print(res)
