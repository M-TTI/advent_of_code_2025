output = 0

with open('day3.input', 'r') as str_input:
    for line in str_input:
        max1 = 0
        max2 = 0
        line = line.strip()
        line_cpy = line

        for i in range(len(line_cpy) - 1):
            if max1 < int(line_cpy[i]):
                max1 = int(line_cpy[i])
                max1_index = i

        line_cpy = line_cpy[max1_index + 1:]
        print(line_cpy)

        for i in range(len(line_cpy)):
            if max2 < int(line_cpy[i]):
                max2 = int(line_cpy[i])

        print(f'max1: {max1}, max2: {max2}')
        output += int(str(max1) + str(max2))

print(output)