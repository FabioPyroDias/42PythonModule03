import math


def create_position(x: int, y: int, z: int) -> tuple:
    return tuple([x, y, z])


def parse_position(pos: str) -> tuple:
    try:
        pos = pos.split(",")
        if len(pos) != 3:
            raise ValueError("Not enough coordinates")
        x = int(pos[0])
        y = int(pos[1])
        z = int(pos[2])
        print(f"Parsed position: ({x}, {y}, {z}")
        return create_position(x, y, z)
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: {type(error).__name__}, Args: {error.args})")
        return None


def distance_between_points(point_start: tuple, point_end: tuple) -> float:
    return math.sqrt((point_end[0] - point_start[0]) ** 2 + (point_end[1] - point_start[1]) ** 2 + (point_end[2] - point_start[2]) ** 2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    origin = tuple([0, 0, 0])
    pos0 = create_position(10, 20, 5)
    print(f"Position created: ({pos0[0]}, {pos0[1]}, {pos0[2]})")
    distance0 = distance_between_points(origin, pos0)
    print(f"Distance between ({origin[0]}, {origin[1]}, {origin[2]}) and ({pos0[0]}, {pos0[1]}, {pos0[2]}): {distance0:.2f}")
    print()
    print("Parsing coordinates: 3,4,0")
    pos1 = parse_position("3,4,0")
    distance1 = distance_between_points(origin, pos1)
    print(f"Distance between ({origin[0]}, {origin[1]}, {origin[2]}) and ({pos1[0]}, {pos1[1]}, {pos1[2]}): {distance1:.1f}")
    print()
    print("Parsing invalid coordinates: \"abc,def,ghi\"")
    parse_position("abc,def,ghi")
    print()
    print("Unpacking demonstration:")
    player = create_position(3, 4, 0)
    print(f"Player at x={player[0]}, y={player[1]}, z={player[2]}")
    x, y, z = player
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
