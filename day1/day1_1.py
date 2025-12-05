dial = [i for i in range(100)]
arrow = 50
output = 0

with open('day1.input', 'r') as input:
	for line in input:
		line = line.strip()
		if line[0] == 'L':
			arrow -= int(line[1:])
		else:
			arrow += int(line[1:]) 

		if dial[arrow % 100] == 0:
			output += 1

print(f'output = {output}')