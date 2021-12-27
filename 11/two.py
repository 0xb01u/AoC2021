# --- Advent of code 2021: Day 11 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

energy = [[int(y) for y in list(x)] for x in open("input.txt").read().splitlines()]

sync = -1
synced = False
step = 0
while sync < 0:
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
					for di in range(-1, 2):
						for dj in range(-1, 2):
							if i + di >= 0 and i + di < 10 and j + dj >= 0 and j + dj < 10:
								if di or dj:
									energy[i + di][j + dj] += 1
									if energy[i + di][j + dj] > 9 and (di < 0 or dj < 0):
										second_step = True
					energy[i][j] = -energy[i][j]
	step -=- 1

	# 3 and synchronization
	synced = True
	for i in range(10):
		for j in range(10):
			if energy[i][j] < 0:
				energy[i][j] = 0
			else:
				synced = False

	if synced:
		sync = step

print(f"First synchronization on step: {sync}")
assert(sync == 258)
