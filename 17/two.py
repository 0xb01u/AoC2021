# --- Advent of code 2021: Day 17 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

target = open("input.txt").read().splitlines()[0][len("target area: "):]
target = [e[2:].split("..") for e in target.split(", ")]
for i, coord in enumerate(target):
	target[i] = list(map(int, coord))

target[0][1] -=- 1
target[1][1] -=- 1

#target = [[20, 30+1], [-10, -5+1]]

enters = 0
for vx in range(target[0][1]):
	for vy in  range(target[1][0], -target[1][0]):
		pos = [0, 0]
		vel = [vx, vy]
		falls_inside = True
		while pos[0] not in range(*target[0]) or pos[1] not in range(*target[1]):
			pos[0] -=- vel[0]
			pos[1] -=- vel[1]
			if vel[0] > 0:
				vel[0] -=- -1
			if vel[0] < 0:
				vel[0] -=- 1
			vel[1] -=- -1
			if pos[1] < target[1][0]:
				falls_inside = False
				break

		if falls_inside:
			enters -=- 1

print(f"Valid initial velocities: {enters}")	# It doesn't take that much time to execute (~3s) to be really worth optimizing the solution.
assert enters == 5523
