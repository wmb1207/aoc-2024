from typing import Generator

delta_by_letters: dict[str, int] = {"m": 1, "a": 2, "s": 3}


def read_input(file_path: str) -> tuple[list[str], int]:
    lines: list[str] = []
    width: int = 0
    with open(file_path, "r") as file:
        for line in file:
            lines.append(line)

            if not width:
                width = len(line)

    print(len(lines))
    joined = "".join(lines)

    return list(joined.lower()), width


def left(
    idx: int, to_found: str, delta_by_letter: int, matrix: list[str], _: int
) -> int:
    lookup_idx = idx + delta_by_letter
    return lookup_idx if matrix[lookup_idx] == to_found else -1


def right(
    idx: int, to_found: str, delta_by_letter: int, matrix: list[str], _: int
) -> int:
    lookup_idx = idx - delta_by_letter
    return lookup_idx if matrix[lookup_idx] == to_found else -1


def bottom(
    idx: int, to_found: str, delta_by_letter: int, matrix: list[str], delta: int
) -> int:
    lookup_idx = idx + delta_by_letter * delta
    return lookup_idx if matrix[lookup_idx] == to_found else -1


def top(
    idx: int, to_found: str, delta_by_letter: int, matrix: list[str], delta: int
) -> int:
    lookup_idx = idx - delta_by_letter * delta
    return lookup_idx if matrix[lookup_idx] == to_found else -1


def left_to_right_top_to_bottom_diag(
    idx: int, to_found: str, delta_by_letter: int, matrix: list[str], delta: int
) -> int:
    lookup_idx = idx + delta_by_letter * delta + delta_by_letter
    return lookup_idx if matrix[lookup_idx] == to_found else -1


def right_to_left_top_to_bottom_diag(
    idx: int, to_found: str, delta_by_letter: int, matrix: list[str], delta: int
) -> int:
    lookup_idx = idx + delta_by_letter * delta - delta_by_letter
    return lookup_idx if matrix[lookup_idx] == to_found else -1


def right_to_left_bottom_to_top_diag(
    idx: int, to_found: str, delta_by_letter: int, matrix: list[str], delta: int
) -> int:
    lookup_idx = idx - delta_by_letter * delta - delta_by_letter
    return lookup_idx if matrix[lookup_idx] == to_found else -1


def left_to_right_bottom_to_top_diag(
    idx: int, to_found: str, delta_by_letter: int, matrix: list[str], delta: int
) -> int:
    lookup_idx = idx - delta_by_letter * delta + delta_by_letter
    return lookup_idx if matrix[lookup_idx] == to_found else -1


def left_top_corner(
    idx: int, matrix: list[str], width: int, expected_letter: str | None = None
) -> int:
    lookup_idx = idx - width - 1
    return (
        lookup_idx
        if matrix[lookup_idx]
        in (["m", "s"] if not expected_letter else [expected_letter])
        else -1
    )


def left_bottom_corner(
    idx: int, matrix: list[str], width: int, expected_letter: str | None = None
) -> int:
    lookup_idx = idx + width - 1
    return (
        lookup_idx
        if matrix[lookup_idx]
        in (["m", "s"] if not expected_letter else [expected_letter])
        else -1
    )


def right_top_corner(
    idx: int, matrix: list[str], width: int, expected_letter: str | None = None
) -> int:
    lookup_idx = idx - width + 1
    return (
        lookup_idx
        if matrix[lookup_idx]
        in (["m", "s"] if not expected_letter else [expected_letter])
        else -1
    )


def right_bottom_corner(
    idx: int, matrix: list[str], width: int, expected_letter: str | None = None
) -> int:
    lookup_idx = idx + width + 1
    return (
        lookup_idx
        if matrix[lookup_idx]
        in (["m", "s"] if not expected_letter else [expected_letter])
        else -1
    )


def x_handler(idx: int, matrix: list[str], delta: int) -> Generator[tuple]:
    for condition in [
        left,
        right,
        top,
        bottom,
        left_to_right_bottom_to_top_diag,
        left_to_right_top_to_bottom_diag,
        right_to_left_bottom_to_top_diag,
        right_to_left_top_to_bottom_diag,
    ]:
        try:
            found = [idx]
            for next in ["m", "a", "s"]:
                pos = condition(idx, next, delta_by_letters[next], matrix, delta)
                if pos > 0:
                    found.append(pos)
                    continue
                break
            if len(found) == 4:
                yield found
        except Exception:
            continue


def a_handler(idx: int, matrix: list[str], delta: int) -> tuple:
    top_left_idx = left_top_corner(idx, matrix, delta)
    if top_left_idx < 0:
        raise Exception("Cannot form an X")
    top_left = matrix[top_left_idx]

    top_right_idx = right_top_corner(idx, matrix, delta)
    if top_right_idx < 0:
        raise Exception("Cannot form an X")
    top_right = matrix[top_right_idx]

    expected: tuple | None = None
    match (top_left, top_right):
        case ("m", "m"):
            expected = ("s", "s")
        case ("s", "s"):
            expected = ("m", "m")
        case ("s", "m"):
            expected = ("s", "m")
        case ("m", "s"):
            expected = ("m", "s")

    if not expected:
        raise Exception("Invalid Expected")

    bottom_left_idx, bottom_right_idx = (
        left_bottom_corner(idx, matrix, delta, expected[0]),
        right_bottom_corner(idx, matrix, delta, expected[1]),
    )

    if bottom_right_idx == -1 or bottom_left_idx == -1:
        raise Exception("Cannot form an X")

    return top_left_idx, top_right_idx, idx, bottom_left_idx, bottom_right_idx


def find(matrix: list[str], width: int) -> int:
    total = 0

    for idx, char in enumerate(matrix):
        if char != "x":
            continue
        for val in x_handler(idx, matrix, width):
            print(val)
            if len(val) == 4:
                total += 1

    return total


def find_cross_mas(
    matrix: list[str], width: int, debug: bool = False
) -> (int, list[int]):
    total = 0
    positions = []
    for idx, char in enumerate(matrix):
        if char != "a":
            continue
        try:
            result = a_handler(idx, matrix, width)
            positions.extend(list(result))
            total += 1
        except Exception as err:
            print(err)
            continue

    return total, positions


def main():
    debug = True
    matrix, width = read_input("input_4.txt")
    print(f"Part 1: {find(matrix, width)}")
    result = find_cross_mas(matrix, width)
    print(f"Part 2: {result[0]}")
    if debug:
        for idx, char in enumerate(matrix):
            if idx not in result[1] and char != "\n":
                matrix[idx] = "."

        with open("debug.txt", "w") as f:
            data = "".join(matrix)
            f.write(data)


if __name__ == "__main__":
    main()
