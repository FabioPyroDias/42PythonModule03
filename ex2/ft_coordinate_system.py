import math


def create_position(coordinates: list) -> tuple:
    """"""
    return tuple(coordinates)


def parse_position(position: str) -> list:
    """"""
    split = position.split(",")
    coordinates = [0] * len(split)
    for index in range(len(split)):
        coordinates[index] = int(split[index])
    return coordinates


def calculate_distance(origin: tuple, target: tuple) -> float:
    """"""
    dst = math.sqrt((target[0] - origin[0])**2 + (target[1] - origin[1])**2 +
                    (target[2] - origin[2])**2)
    return dst


def test_example(example: int):
    """"""
    origin = tuple([0, 0, 0])
    if example == 0:
        pos = create_position([10, 20, 5])
        print(f"Position created: {pos}")
        dst = calculate_distance(origin, pos)
        print(f"Distance between {origin} and {pos}: {dst:.2f}")
    elif example == 1:
        print("Parsing coordinates: \"3,4,0\"")
        coordinates = parse_position("3,4,0")
        pos = create_position(coordinates)
        print(f"Parsed position: {pos}")
        dst = calculate_distance(origin, pos)
        print(f"Distance between {origin} and {pos}: {dst:.1f}")
    elif example == 2:
        print("Parsing invalid coordinates: \"abc,def,ghi\"")
        try:
            parse_position("abc,def,ghi")
        except ValueError as error:
            print(f"Error parsing coordinates: {error}")
            print(f"Error details - Type: {type(error).__name__}, Args: "
                  f"{error.args}")
    elif example == 3:
        print("Unpacking demonstration:")
        x, y, z = create_position([3, 4, 0])
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


def test_exercise() -> None:
    """"""
    print("=== Game Coordinate System ===")
    print()
    test_example(0)
    print()
    test_example(1)
    print()
    test_example(2)
    print()
    test_example(3)

if __name__ == "__main__":
    test_exercise()