output = 0

with open('day3_test.input', 'r') as str_input:
    for line in str_input:
        new_number = ''
        exclude_last_digits = 11
        max_index = 0

        while exclude_last_digits > 0:
            line_cpy = line.strip()[max_index:]
            print(f'line_cpy: {line_cpy}')
            max_digit = 0

            for i in range(len(line_cpy)):
                if max_digit < int(line_cpy[i]):
                    max_digit = int(line_cpy[i])
                    max_index = i

                new_number += str(max_digit)
                exclude_last_digits -= 1

        print(new_number)