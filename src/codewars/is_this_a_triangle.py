def is_triangle(a: int, b: int, c: int) -> bool:
    return (a > 0 and b > 0 and c > 0) and (a + b > c and b + c > a and a + c > b)


if __name__ == "__main__":
    a = int(input("Lenght of segment 1: "))
    b = int(input("Lenght of segment 2: "))
    c = int(input("Lenght of segment 3: "))  # Defined our segments
    res = is_triangle(a, b, c)

    print(res)  # Displays result on the screen
