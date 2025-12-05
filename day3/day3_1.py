max1 = 0
max2 = 0

with open('day3.input', 'r') as input:
	for line in input:
		max1 = 0
		max2 = 0
		line = line.strip()
		line_cpy = line

		for i in range(len(line_cpy)):
			if max1 < int(line_cpy[i]):
				max1 = int(line_cpy[i])
				max1_index = i

		line_cpy.replace(str(max1), '', 1)

		for i in range(len(line_cpy[i])):
			if max2 < int(line_cpy[i]):
				max2 = int(line_cpy[i])
				max2_index = 2

		print(f'max1: {max1}, max2: {max2}')