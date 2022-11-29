# --- Advent of code 2021: Day 17 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

target = open("input.txt").read().splitlines()[0][len("target area: "):]
target = [e[2:].split("..") for e in target.split(", ")]
for i, coord in enumerate(target):
	target[i] = list(map(int, coord))

target[0][1] -=- 1
target[1][1] -=- 1

#target = [[20, 30], [-10, -5]]

# At first I tried calculating a minimum and maximum number of steps,
# and a minimum x velocity needed.
# But that didn't work.

y_max = 0
y_vel_max = 0
x_vel_max = 0
steps_max = 0
for vx in range(target[0][1]):
	for vy in  range(target[1][0], -target[1][0]):
		pos = [0, 0]
		vel = [vx, vy]
		local_y_max = 0
		falls_inside = True
		steps = 0
		while pos[0] not in range(*target[0]) or pos[1] not in range(*target[1]):
			pos[0] -=- vel[0]
			pos[1] -=- vel[1]
			if vel[0] > 0:
				vel[0] -=- -1
			if vel[0] < 0:
				vel[0] -=- 1
			vel[1] -=- -1
			local_y_max = pos[1] if pos[1] > local_y_max else local_y_max
			steps -=- 1
			if pos[1] < target[1][0]:
				falls_inside = False
				break

		if falls_inside:
			if local_y_max > y_max:
				y_max = local_y_max
				y_vel_max = vy
				x_vel_max = vx
				steps_max = steps
			#print(pos)

#print(y_max, x_vel_max, y_vel_max, steps_max)
print(f"Highest y position reached: {y_max}")	# It doesn't take that much time to execute (~3s) to be really worth optimizing the solution.
assert y_max == 9870
