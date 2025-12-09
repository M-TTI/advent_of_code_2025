def is_forkliftable(current_roll_index, current_row, upper_row = None, lower_row = None):
	places_to_check = []
	roll_counter = 0

	if current_roll_index == 0:
		if upper_row == None:
			places_to_check.extend([
				current_row[current_roll_index + 1], 
				lower_row[current_roll_index], 
				lower_row[current_roll_index + 1],
			])
		elif lower_row == None:
			places_to_check.extend([
				upper_row[current_roll_index + 1], 
				upper_row[current_roll_index],
				current_row[current_roll_index + 1], 
			])
		else:
			places_to_check.extend([
				upper_row[current_roll_index + 1], 
				upper_row[current_roll_index],
				current_row[current_roll_index + 1],
				lower_row[current_roll_index], 
				lower_row[current_roll_index + 1],
			])

	elif current_roll_index == len(current_row) - 1:
		if upper_row == None:
			places_to_check.extend([
				current_row[current_roll_index - 1], 
				lower_row[current_roll_index - 1], 
				lower_row[current_roll_index],
			])
		elif lower_row == None:
			places_to_check.extend([
				upper_row[current_roll_index], 
				upper_row[current_roll_index - 1],
				current_row[current_roll_index - 1], 
			])
		else:
			places_to_check.extend([
				upper_row[current_roll_index], 
				upper_row[current_roll_index - 1],
				current_row[current_roll_index - 1],
				lower_row[current_roll_index - 1], 
				lower_row[current_roll_index],
			])

	else:
		if upper_row == None:
			places_to_check.extend([
				current_row[current_roll_index - 1],
				lower_row[current_roll_index - 1],
				lower_row[current_roll_index],
				lower_row[current_roll_index + 1],
				current_row[current_roll_index + 1],
			])
		elif lower_row == None:
			places_to_check.extend([
				current_row[current_roll_index + 1],
				upper_row[current_roll_index + 1],
				upper_row[current_roll_index], 
				upper_row[current_roll_index - 1],
				current_row[current_roll_index - 1], 
			])
		else:
			places_to_check.extend([
				upper_row[current_roll_index + 1],
				upper_row[current_roll_index], 
				upper_row[current_roll_index - 1],
				current_row[current_roll_index - 1],
				lower_row[current_roll_index - 1], 
				lower_row[current_roll_index],
				lower_row[current_roll_index + 1],
				current_row[current_roll_index + 1]
			])

	for roll in places_to_check:
		# print(f'current_roll_index: {current_roll_index}, roll: {roll}')
		roll_counter += 1 if roll == '@' else 0

	return roll_counter < 4


def str_replace(string, new_char, index):
	assert index in range(len(string))

	return string[:index] + new_char + string[index + 1:]


count_forkliftable = 0
grid = []
new_grid = []
forkliftable_rolls_left = True

with open('day4.input', 'r') as file:
	for line in file:
		line = line.strip()
		grid.append(line)


while forkliftable_rolls_left:
	upper_row = None
	lower_row = grid[1]
	forkliftable_rolls_left = False

	for row_index in range(len(grid)):
		row = grid[row_index]
		new_row = row
		lower_row = grid[row_index + 1] if row_index < len(row) - 1 else None

		for current_index in range(len(row)):
			if row[current_index] == '@':
				if is_forkliftable(current_index, row, upper_row, lower_row):
					count_forkliftable += 1
					new_row = str_replace(new_row, 'x', current_index)
					forkliftable_rolls_left = True

		new_grid.append(new_row)
		upper_row = row

	grid = new_grid[:]
	new_grid.clear()
	for row in grid:
		print(row)
	print()


print(count_forkliftable)