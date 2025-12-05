def has_repeated_sequence(s: str) -> bool:
	new_s = ''
	for char in s[:len(s) // 2]:
		repeated_s = ''
		new_s += char
		while len(repeated_s) < len(s):
			repeated_s += new_s
		if repeated_s == s:
			return True
	return False

output = 0

with open('day2.input', 'r') as input:
	input_array = input.readline().split(',')

for ids in input_array:
	first_id, last_id = ids.split('-')
	for i in range(int(first_id), int(last_id) + 1):
		if has_repeated_sequence(str(i)):
			output += i

print(output)