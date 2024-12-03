import re

def read_input(file_name: str) -> str:
    output = ""
    with open(file_name, 'r') as file:
        for line in file:
            output += line


    output = output.replace("\r", "").replace("\n", "")
    with open('test.input', 'w') as file:
        file.write(output)

    return output


mul_regex = r"mul\([0-9]*,[0-9]*\)"

#invalid_spaces_regex = r"don't\(\).*?(do\(\)|$)"

def step_one(content: str) -> int:
    matches = re.findall(mul_regex, content, re.IGNORECASE)
    groups = [eval(m.replace('mul', '')) for m in matches]
    return sum([g[0] * g[1] for g in groups])


def step_two(content: str) -> int:
    mul_regex = r"mul\([0-9]*,[0-9]*\)|do\(\)|don\'t\(\)"
    cases = re.findall(mul_regex, content, re.IGNORECASE)

    total_flag = True
    total = 0
    for case in cases:
        if case == "don't()":
            total_flag = False
            continue

        if case == 'do()':
            total_flag = True
            continue

        if total_flag:
            a, b = eval(case.replace('mul', ''))
            total += a * b

    return total
        


    

    #valid_text = re.sub(invalid_spaces_regex, "", content, flags=re.IGNORECASE)
    # breakpoint()
    # return step_one(valid_text)

def main():
    content = read_input('input_3.txt')
    result = step_one(content)
    print(f"Step one: {result}")
    result = step_two(content)
    print(f"Step two: {result}")


if __name__ == '__main__':
    main()
