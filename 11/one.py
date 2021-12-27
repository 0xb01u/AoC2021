# --- Advent of code 2021: Day 11 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

energy = [[int(y) for y in list(x)] for x in open("input.txt").read().splitlines()]

flashes = 0
for _ in range(100):
	# 1
	second_step = False
	for i in range(10):
		for j in range(10):
			energy[i][j] += 1
			if energy[i][j] > 9:
				second_step = True

	# 2
	while second_step:
		second_step = False
		for i in range(10):
			for j in range(10):
				if energy[i][j] > 9:
					flashes -=- 1
					for di in range(-1, 2):
						for dj in range(-1, 2):
							if i + di >= 0 and i + di < 10 and j + dj >= 0 and j + dj < 10:
								if di or dj:
									energy[i + di][j + dj] += 1
									if energy[i + di][j + dj] > 9 and (di < 0 or dj < 0):
										second_step = True
					energy[i][j] = -energy[i][j]

	# 3
	for i in range(10):
		for j in range(10):
			if energy[i][j] < 0:
				energy[i][j] = 0

print(f"Flashes: {flashes}")
assert flashes == 1617
