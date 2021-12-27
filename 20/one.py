# --- Advent of code 2021: Day 20 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

algorithm, image = open("input.txt").read().split("\n\n")
image = image.splitlines()

lit_pixels = {(i, j) for i in range(len(image)) for j in range(len(image[i])) if image[i][j] == '#'}

def i2o(image, black=False):
	global algorithm

	_x = min({e[0] for e in image})
	_y = min({e[1] for e in image})
	x = max({e[0] for e in image}) + 1
	y = max({e[1] for e in image}) + 1

	out = set()
	for i in range(_x - 2, x + 2):
		for j in range(_y - 2, y + 2):
			binnum = 0
			for di in range(-1, 2):
				for dj in range(-1, 2):
					binnum <<= 1
					if (i + di, j + dj) in image:
						binnum |= 1
					elif ((i + di) < _x or (i + di) >= x or (j + dj) < _y or (j + dj) >= y) and (algorithm[0] == '#' and not black):
						binnum |= 1						

			if algorithm[binnum] == '#':
				out.add((i, j))

	'''
	for i in range(_x - 2, x + 2):
		for j in range(_y - 2, y + 2):
			if (i, j) in image:
				print("#", end="")
			else:
				print(".", end="")
		print()
	print()
	'''

	return out

res = i2o(i2o(lit_pixels, True))

print(f"Lit pixels in the resulting image: {len(res)}")
assert len(res) == 5425
