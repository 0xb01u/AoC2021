# --- Advent of code 2021: Day 22 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

instructions = open("input.txt").read().splitlines()

cubes_on = set()
for ins in instructions:
	range_x, range_y, range_z = [sorted([int(x) for x in e[2:].split("..")]) for e in ins[len(ins.split(" ")[0]) + 1:].split(",")]

	dx = range_x[1] - range_x[0]
	dy = range_y[1] - range_y[0]
	dz = range_z[1] - range_z[0]

	if 50 < range_x[0] or -50 > range_x[1]:
		dx = 0
	if 50 < range_y[0] or -50 > range_y[1]:
		dy = 0
	if 50 < range_z[0] or -50 > range_z[1]:
		dz = 0

	if dx * dy * dz > 0:	
		for i in range(range_x[0], range_x[1] + 1):
			for j in range(range_y[0], range_y[1] + 1):
				for k in range(range_z[0], range_z[1] + 1):
					if "off" in ins:
						if (i, j, k) in cubes_on:
							cubes_on.remove((i, j, k))
					else:
						cubes_on.add((i, j, k))

print(f"Amount of cubes that are on: {len(cubes_on)}")
assert len(cubes_on) == 607573
