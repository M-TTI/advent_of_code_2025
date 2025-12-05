def has_doubled_sequence(s: str) -> bool:
	first_half, last_half = split_in_half(s)
	return first_half == last_half


def split_in_half(s: str) -> tuple:
	mid = len(s) // 2
	return s[:mid], s[mid:]

output = 0

with open('day2.input', 'r') as str_input:
	for line in str_input:
		input_array = line.split(',')

for ids in input_array:
	first_id, last_id = ids.split('-')
	for i in range(int(first_id), int(last_id) + 1):
		if has_doubled_sequence(str(i)):
			output += i

print(output)