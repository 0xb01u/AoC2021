# --- Advent of code 2021: Day 09 ---

# (File automatically generated by aocTool, developed by Bolu, 2020-2021.)

heightmap = open("input.txt").read().splitlines()

low_points = []

for i in range(len(heightmap)):
	for j in range(len(heightmap[i])):
		height = heightmap[i][j]
		print(height)
		exit()
		low = True
		if i > 0:
			low &= height < heightmap[i - 1][j]
		if j > 0:
			low &= height < heightmap[i][j - 1]
		if i < len(heightmap) - 1:
			low &= height < heightmap[i + 1][j]
		if j < len(heightmap[i]) - 1:
			low &= height < heightmap[i][j + 1]

		if low:
			low_points.append(height)

print(f"Sum of the risk levels: {sum([int(x) for x in low_points]) + len(low_points)}")
assert (sum([int(x) for x in low_points]) + len(low_points)) == 489
