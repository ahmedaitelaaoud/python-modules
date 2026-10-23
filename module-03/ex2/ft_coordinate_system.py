"""Exercise 2: Coordinate System.

Work with tuples and basic geometry in a simple 3D world.
"""

import sys



def cal_distance(p1, p2):
    """Return the Euclidean distance between two 3D points."""
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2) ** 0.5


def parsing_coor(coor):
    """Parse a comma-separated coordinate string into a 3D tuple."""
    parts = coor.split(",")
    if len(parts) != 3:
        raise ValueError(f"Expected 3 coordinates, got {len(parts)}")
    x, y, z = int(parts[0]), int(parts[1]), int(parts[2])
    return (x, y, z)


def demonstration(p):
    """Print the unpacked coordinate values."""
    x, y, z = p
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main():
    """Run the coordinate system demo."""
    print("=== Game Coordinate System ===\n")
    init_position = (0, 0, 0)
    if len(sys.argv) > 1:
        for coord_str in sys.argv[1:]:
            try:
                print(f"\nParsing coordinates: \"{coord_str}\"")
                parsed_pos = parsing_coor(coord_str)
                print(f"Parsed position: {parsed_pos}")
                distance = cal_distance(init_position, parsed_pos)
                print(f"Distance between {init_position} and {parsed_pos}: "
                      f"{distance:.2f}")
                print("\nUnpacking demonstration:")
                demonstration(parsed_pos)
            except ValueError as e:
                print(f"Error parsing coordinates: {e}")

    else:
        new_position = (10, 20, 5)
        print(f"Position created: {new_position}")
        distance = cal_distance(init_position, new_position)
        print(f"Distance between {init_position} and {new_position}: "
              f"{distance:.2f}")
        print("\nParsing coordinates: \"3,4,0\"")
        try:
            teleport = parsing_coor("3,4,0")
            print(f"Parsed position: {teleport}")
            distance = cal_distance(init_position, teleport)
            print(f"Distance between {init_position} and {teleport}: "
                  f"{distance}")
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
        print("\nParsing invalid coordinates: \"abc,def,ghi\"")
        try:
            parsing_coor("abc,def,ghi")
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {type(e).__name__}, "
                  f"Args: {e.args}")
        print("\nUnpacking demonstration:")
        demonstration(teleport)


if __name__ == "__main__":
    main()
