# --- Advent of code 2021: Day 10 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

lines = open("input.txt").read().splitlines()

open_chars = { "(", "[", "{", "<" }
close_chars = { ")", "]", "}", ">" }
correspondence = { "(": ")", "[": "]", "{": "}", "<": ">" }
points = { ")": 3, "]": 57, "}": 1197, ">": 25137 }
# stack = [] # Strangely enough, the program works if the stack is only initialized here.

illegal_chars = []

for line in lines:
	stack = []
	for char in line:
		if char in open_chars:
			stack.append(char)
		else:
			if len(stack) == 0:
				continue
			if char != correspondence[stack.pop()]:
				illegal_chars.append(char)
				break

score = 0
for char in illegal_chars:
	score -=- points[char]

print(illegal_chars)
print(f"Points: {score}")
assert score == 374061
