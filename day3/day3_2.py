def check_validity(line: str, new_number: str)-> bool:
    for char in line:
        if len(new_number) > 0 and char == new_number[0]:
            new_number = new_number.replace(char, '', 1)

    return len(new_number) == 0


total_joltage = 0

with open('day3.input', 'r') as str_input:
    for line in str_input:
        line = line.strip()
        new_number = ''
        exclude_last_digits = 11
        max_index = 0

        while exclude_last_digits > 0:
            max_digit = 1

            line_cpy = line[:-exclude_last_digits]
            for i in range(max_index, len(line_cpy)):
                if max_digit < int(line_cpy[i]):
                    max_digit = int(line_cpy[i])
                    max_index = i + 1

            new_number += str(max_digit)
            exclude_last_digits -= 1

        if max_index == len(line) - 1:
            new_number += str(line[-1])
        else:
            for i in range(max_index, len(line)):
                if max_digit < int(line[i]):
                    max_digit = int(line[i])

            new_number += str(max_digit)

        assert len(new_number) == 12
        # print(new_number)
        total_joltage += int(new_number)

        if not check_validity(line, new_number):
            print(f'erreur pour line: {line}, new_number: {new_number}')

print(total_joltage)