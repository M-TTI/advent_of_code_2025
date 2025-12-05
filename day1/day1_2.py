# dial = 50
# output = 0

# with open('day1.input', 'r') as str_input:
# 	for line in str_input:
# 		line = line.strip()
# 		rotation_value = int(line[1:])

# 		if line[0] == 'L':
# 			dial -= rotation_value
# 		elif line[0] == 'R':
# 			dial += rotation_value

# 		output += abs(dial // 100)

# 		if dial <= 0:
# 			output += 1

# 		dial = dial % 100

# 		print(f'output: {output}, dial: {dial}, line: {line}')

# print(f'output = {output}')


# This didnt work so i gave up and simulated the dial instead

dial = 50
output = 0

with open('day1.input', 'r') as str_input:
	for line in str_input:
		line = line.strip()
		rotation_value = int(line[1:])

		if line[0] == 'L':
			for i in range(rotation_value):
				dial -= 1
				if dial == 0:
					output += 1
				if dial == -1:
					dial = 99
		elif line[0] == 'R':
			for i in range(rotation_value):
				dial += 1
				if dial == 100:
					dial = 0
					output += 1

print(output)