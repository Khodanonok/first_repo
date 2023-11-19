from math import sqrt


def is_triangle(a: int, b: int, c: int) -> bool:
    return (a > 0 and b > 0 and c > 0) and (a + b > c and b + c > a and a + c > b)


def find_possible_third_side(a: int, b: int) -> list[int]:
    possible_sides = []  # created a list for substitution of c values

    for c in range((b - a) + 1, a + b):
        # loop in range from minimal to maximal possible value of c
        if c != (a * a + b * b) ** 0.5:
            # iterating each value (except hypotenuse)
            possible_sides.append(c)  # add acceptable values to the list

    return possible_sides


def belo_possibilities(a: int, b: int) -> list[int]:
    """returns: a list of side.."""
    possible_sides = list(range((b - a) + 1, a + b))
    possible_sides.remove((a * a + b * b) ** 0.5)
    return possible_sides


def easy_possibilities(a, b):
    """Look up Python List Comprehension"""
    return [c for c in range((b - a) + 1, a + b) if c != sqrt(a * a + b * b)]


if __name__ == "__main__":
    a = int(input("Lenght of segment 1: "))
    b = int(input("Lenght of segment 2: "))
    c = int(input("Lenght of segment 3: "))  # Defined our segments

    print(is_triangle(a, b, c))
