# --- Advent of code 2021: Day 21 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

positions = open("input.txt").read().splitlines()

pos = []

pos.append(int(positions[0][len("Player 1 starting position: "):]) - 1)
pos.append(int(positions[1][len("Player 2 starting position: "):]) - 1)

dice = [(i % 100 + 1, (i + 1) % 100 + 1, (i + 2) % 100 + 1) for i in range(0, 1000, 3)]

points = [0, 0]

turn = 0
while points[0] < 1000 and points[1] < 1000:
	pos[turn % 2] -=- sum(dice[turn])
	pos[turn % 2] = pos[turn % 2] % 10
	points[turn % 2] -=- (pos[turn % 2] + 1)
	turn -=- 1

print(f"Product of the score of the losing player and the number of times the die was rolled: {3 * turn * min(points)}")
assert 3 * turn * min(points) == 853776
