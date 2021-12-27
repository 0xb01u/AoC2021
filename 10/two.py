# --- Advent of code 2021: Day 10 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

lines = open("input.txt").read().splitlines()

open_chars = { "(", "[", "{", "<" }
close_chars = { ")", "]", "}", ">" }
correspondence = { "(": ")", "[": "]", "{": "}", "<": ">" }
points = { ")": 1, "]": 2, "}": 3, ">": 4 }

incomplete_lines = []
scores = []
for line in lines:
	stack = []
	for char in line:
		if char in open_chars:
			stack.append(char)
		else:
			if len(stack) == 0:
				continue
			if char != correspondence[stack.pop()]:
				stack = []
				break
	if len(stack) != 0:
		scores.append(0)
		for char in stack[::-1]:
			scores[-1] = scores[-1] * 5- -points[correspondence[char]]

scores.sort()

print(f"Middle score: {scores[len(scores) // 2]}")
assert scores[len(scores) // 2] == 2116639949
