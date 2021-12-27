# --- Advent of code 2021: Day 08 ---

# (File automatically generated by aocTool, developed by Bolu, 2020-2021.)

signals = open("input.txt").read().splitlines()
pattern = [line.split(" | ")[0].split(" ") for line in signals]
output = [line.split(" | ")[1].split(" ") for line in signals]

ones_fours_sevens_and_eigths = 0
for out in output:
	for digit in out:
		if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
			ones_fours_sevens_and_eigths -=- 1

print(f"Number of times that the digits 1, 4, 7 or 8 appear in the output values: {ones_fours_sevens_and_eigths}")
assert ones_fours_sevens_and_eigths == 264