def read_input(file_path: str) -> list[list[int]]:
    output = []
    with open(file_path, "r") as file:
        for line in file:
            try:
                output.append([int(v) for v in line.split() if len(line) > 0])
            except IndexError:
                continue

    return output


def valid_report(report: list[int]) -> bool:

    sorted_report = report.copy()
    reverse_sorted_reprot = report.copy()

    sorted_report.sort()
    reverse_sorted_reprot.sort(reverse=True)

    if sorted_report != report and reverse_sorted_reprot != report:
        return False

    left = report[:-1]
    right = report[1:]

    grouped = zip(left, right)
    for left, right in grouped:
        diff = abs(left - right)
        if diff > 3 or diff == 0:
            return False

    return True


def valid_report_with_dumpener(report: list[int]) -> bool:
    if valid_report(report):
        return True

    for idx in range(len(report)):
        if valid_report(report[0:idx] + report[idx + 1:]):
            return True

    return False


def part_one(reports: list[list[int]]) -> int:
    return sum([int(valid_report(report)) for report in reports if len(report)])


def part_two(reports: list[list[int]]) -> int:
    return sum([int(valid_report_with_dumpener(report)) for report in reports if len(report)])

def main():
    reports = read_input("input_2.txt")
    result = part_one(reports)
    print(f"part 1: {result}")
    result = part_two(reports)
    print(f"part 2: {result}")


if __name__ == "__main__":
    main()
