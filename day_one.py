from typing import OrderedDict


def load_data(file_path: str) -> tuple[list[int], list[int]]:
    left = []
    right = []
    with open(file_path, "r") as data:
        for line in data:
            try:
                splitted_data = line.split()
                left.append(int(splitted_data[0]))
                right.append(int(splitted_data[-1]))
            except IndexError:
                continue

    return left, right


def first_part(left: list[int], right: list[int]) -> int:

    left.sort()
    right.sort()

    return sum([abs(l - r) for l, r in zip(left, right)])


def second_part(left: list[int], right: list[int]) -> int:
    left.sort()
    right.sort()

    grouped_right = OrderedDict()

    for val in right:
        grouped_right.setdefault(val, []).append(val)

    return sum([l * len(grouped_right[l]) if l in grouped_right else 0 for l in left])


def main():
    left, right = load_data("input_1.txt")
    result = first_part(left, right)
    print(f"Part 1: {result}")
    result = second_part(left, right)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
