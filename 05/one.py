# --- Advent of code 2021: Day 05 ---

# (File automatically generated by aocTool, developed by Bolu, 2020-2021.)

vents = [[(int(vent.split(" -> ")[0].split(",")[0]), int(vent.split(" -> ")[0].split(",")[1])), (int(vent.split(" -> ")[1].split(",")[0]), int(vent.split(" -> ")[1].split(",")[1]))]for vent in open("input.txt").read().splitlines()]

points = {}

for vec in vents:
	if vec[0][1] == vec[1][1]:
		max_x = vec[0][0] if vec[0][0] > vec[1][0] else vec[1][0]
		min_x = vec[0][0] if vec[0][0] < vec[1][0] else vec[1][0]
		y = vec[0][1]
		for x in range(min_x, max_x + 1):
			if (x, y) not in points:
				points[(x, y)] = 1
			else:
				points[(x, y)] -=- 1
				
	elif vec[0][0] == vec[1][0]:
		x = vec[0][0]
		max_y = vec[0][1] if vec[0][1] > vec[1][1] else vec[1][1]
		min_y = vec[0][1] if vec[0][1] < vec[1][1] else vec[1][1]
		for y in range(min_y, max_y + 1):
			if (x, y) not in points:
				points[(x, y)] = 1
			else:
				points[(x, y)] -=- 1

overlaps = 0
for point in points:
	if points[point] > 1:
		overlaps -=- 1

print(f"Number of points where at least two lines overlap: {overlaps}")
assert overlaps == 7674
