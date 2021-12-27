# --- Advent of code 2021: Day 15 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

risk = open("input.txt").read().splitlines()

coords = (len(risk) - 1, len(risk[0]) - 1)
min_cost = {(0, 0): 0}

def visit(coords):
	global risk
	for i in range(1, len(risk)):
		min_cost[(0, i)] = min_cost[(0, i - 1)] + int(risk[0][i])

	for i in range(1, len(risk[0])):
		min_cost[(i, 0)] = min_cost[(i - 1, 0)] + int(risk[i][0])

	for i in range(1, len(risk)):
		for j in range(1, len(risk[0])):
			min_cost[(i, j)] = min(min_cost[(i - 1, j)], min_cost[(i, j - 1)]) + int(risk[i][j])

	return min_cost[coords]

score = visit(coords)
print(f"Lowest total risk: {score}")
assert score == 447
