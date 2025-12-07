total_joltage = 0
break_check = False

with open('day3.input', 'r') as str_input:
    for line in str_input:
        line = line.strip()
        new_number = ''
        exclude_last_digits = 11
        max_index = 0

        while exclude_last_digits > 0:
            if max_index + exclude_last_digits == len(line) - 1:
                for i in range(max_index, len(line)):
                    new_number += str(line[i])
                max_index = len(line)
                break_check = True
                break
            max_digit = 1

            line_cpy = line[:-exclude_last_digits]
            for i in range(max_index, len(line_cpy)):
                if max_digit < int(line_cpy[i]):
                    max_digit = int(line_cpy[i])
                    max_index = i + 1

            new_number += str(max_digit)
            print(f'line_cpy: {line_cpy}, max_index: {max_index}, exclude_last_digits: {exclude_last_digits}, new_number: {new_number}')
            exclude_last_digits -= 1
        if not break_check:
            line_cpy = line
            for i in range(max_index, len(line_cpy)):
                if max_digit < int(line_cpy[i]):
                    max_digit = int(line_cpy[i])

            new_number += str(max_digit)

        print(f'line_cpy: {line_cpy}, max_index: {max_index}, exclude_last_digits: {exclude_last_digits}, new_number: {new_number}')

        assert len(new_number) == 12
        print(new_number)
        total_joltage += int(new_number)

print(total_joltage)