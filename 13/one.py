# --- Advent of code 2021: Day 13 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

dots, folds = [e.splitlines() for e in open("input.txt").read().split("\n\n")]

dots = set(map(lambda x: (int(x.split(",")[0]), int(x.split(",")[1])), dots))
folds = [(x[len("fold along ")], int(x[len("fold along x="):])) for x in folds]

for axis, coord in folds:
	new_dots = set()
	for x, y in dots:
		if axis == 'x':
			if x < coord:
				new_dots.add((x, y))
			elif x > coord:
				new_dots.add((((coord - (x % coord)) % coord), y))
		else:
			if y < coord:
				new_dots.add((x, y))
			elif y > coord:
				new_dots.add((x, ((coord - (y % coord)) % coord)))
	dots = new_dots
	break

print(f"Number of dots visible after first fold: {len(dots)}")
assert len(dots) == 781
