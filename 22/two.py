# --- Advent of code 2021: Day 22 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

class Cube():
	def __init__(self, range_x, range_y, range_z, light="on"):
		self.x = sorted(range_x[:])
		self.y = sorted(range_y[:])
		self.z = sorted(range_z[:])
		self.type = light

	def intersection(self, other):
		if (self.x[0] > other.x[1] or self.x[1] < other.x[0] or
			self.y[0] > other.y[1] or self.y[1] < other.y[0] or
			self.z[0] > other.z[1] or self.z[1] < other.z[0]):
				return None

		return Cube(
			[max(self.x[0], other.x[0]), min(self.x[1], other.x[1])],
			[max(self.y[0], other.y[0]), min(self.y[1], other.y[1])],
			[max(self.z[0], other.z[0]), min(self.z[1], other.z[1])]
			)

	# UNUSED
	def difference(self, other):
		intersection = self.intersection(other)
		if intersection == None:
			return self

		range_x = [0, 0]
		range_y = [0, 0]
		range_z = [0, 0]

		if self.x[0] < intersection.x[0]:
			range_x = [self.x[0], intersection.x[0]]
		elif self.x[1] > intersection.x[1]:
			range_x = [intersection.x[1], self.x[1]]

		if self.y[0] < intersection.y[0]:
			range_y = [self.y[0], intersection.y[0]]
		elif self.y[1] > intersection.y[1]:
			range_y = [intersection.y[1], self.y[1]]

		if self.z[0] < intersection.z[0]:
			range_z = [self.x[0], intersection.z[0]]
		elif self.z[1] > intersection.z[1]:
			range_z = [intersection.z[1], self.z[1]]

	def cardinality(self):
		return (self.x[1] - self.x[0] + 1) * (self.y[1] - self.y[0] + 1) * (self.z[1] - self.z[0] + 1)

	def __add__(self, other):
		assert self.type == "on" and other.type == "on"

		intersection = self.intersection(other)
		if intersection == None:
			return [other]

		extra = []
		if self.x[0] > other.x[0]:
			extra.append(Cube([other.x[0], self.x[0] - 1], other.y, other.z, "on"))
		if self.x[1] < other.x[1]:
			extra.append(Cube([self.x[1] + 1, other.x[1]], other.y, other.z, "on"))
		if self.y[0] > other.y[0]:
			extra.append(Cube(intersection.x, [other.y[0], self.y[0] - 1], other.z, "on"))
		if self.y[1] < other.y[1]:
			extra.append(Cube(intersection.x, [self.y[1] + 1, other.y[1]], other.z, "on"))
		if self.z[0] > other.z[0]:
			extra.append(Cube(intersection.x, intersection.y, [other.z[0], self.z[0] - 1], "on"))
		if self.z[1] < other.z[1]:
			extra.append(Cube(intersection.x, intersection.y, [self.z[1] + 1, other.z[1]], "on"))

		return extra

	def __sub__(self, other):
		assert self.type == "on" and other.type == "off"

		intersection = self.intersection(other)
		if intersection == None:
			return [self]

		extra = []
		if self.x[0] < other.x[0]:
			extra.append(Cube([self.x[0], other.x[0] - 1], self.y, self.z, "on"))
		if self.x[1] > other.x[1]:
			extra.append(Cube([other.x[1] + 1, self.x[1]], self.y, self.z, "on"))
		if self.y[0] < other.y[0]:
			extra.append(Cube(intersection.x, [self.y[0], other.y[0] - 1], self.z, "on"))
		if self.y[1] > other.y[1]:
			extra.append(Cube(intersection.x, [other.y[1] + 1, self.y[1]], self.z, "on"))
		if self.z[0] < other.z[0]:
			extra.append(Cube(intersection.x, intersection.y, [self.z[0], other.z[0] - 1], "on"))
		if self.z[1] > other.z[1]:
			extra.append(Cube(intersection.x, intersection.y, [other.z[1] + 1, self.z[1]], "on"))

		return extra

	def __eq__(self, other):
		if other == None:
			return False
		return self.x == other.x and self.y == other.y and self.z == other.z

	def __repr__(self):
		return f"({self.type}) x={self.x[0]}..{self.x[1]}, y={self.y[0]}..{self.y[1]}, z={self.z[0]}..{self.z[1]}"

	def __hash__(self):
		return hash((tuple(self.x), tuple(self.y), tuple(self.z)))

''' TESTING STUFF
# Test the Cube class:

# Naive tests:
a = Cube([11, 13], [11, 13], [11, 13])
b = Cube([10, 14], [10, 14], [10, 14])
c = Cube([11, 13], [11, 13], [11, 13], "off")
# print(a.cardinality(), b.cardinality())
assert a.cardinality() == 27 and b.cardinality() == 125
# print(a.intersection(b), a.intersection(b).cardinality()) # 27
assert a.intersection(b).cardinality() == 27
# print(a + b, [x.cardinality() for x in a + b]) # [25, 25, 15, 15, 9, 9]
assert [x.cardinality() for x in a + b] == [25, 25, 15, 15, 9, 9]
# print(b - c, [x.cardinality() for x in b - c]) # [25, 25, 15, 15, 9, 9]
assert [x.cardinality() for x in b - c] == [25, 25, 15, 15, 9, 9]
# exit()

# Tests over the initialization procedure region:
instructions = open("input.txt").read().splitlines()

init_cubes_on = set()
cubes = []
delta_sizes1 = []
delta_sizes2 = []
for i, ins in enumerate(instructions):
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

	# Only use init (small) cubres:
	if dx * dy * dz == 0:
		continue
	cubes.append(Cube(range_x, range_y, range_z, ins.split(" ")[0]))

	init_size = len(init_cubes_on)
	for i in range(range_x[0], range_x[1] + 1):
		for j in range(range_y[0], range_y[1] + 1):
			for k in range(range_z[0], range_z[1] + 1):
				if "off" in ins:
					if (i, j, k) in init_cubes_on:
						init_cubes_on.remove((i, j, k))
				else:
					init_cubes_on.add((i, j, k))
	print(f"Iter {i} change: {len(init_cubes_on) - init_size}")
	delta_sizes1.append(len(init_cubes_on) - init_size)

print()

# Init cubes and big cubes do not overlap.
res = []
for i, cube in enumerate(cubes):
	init_size = sum([c.cardinality() for c in res])
	if cube.type == "on":
		cur = [cube]
		for already in res:
			nxt = []
			for c in cur:
				nxt.extend(already + c)
			cur = nxt
		res.extend(cur)
	elif cube.type == "off":
		nxt = []
		for already in res:
			nxt.extend(already - cube)
		res = nxt
	print(f"Iter {i} change: {sum([c.cardinality() for c in res]) - init_size}")
	delta_sizes2.append(sum([c.cardinality() for c in res]) - init_size)

assert delta_sizes1 == delta_sizes2
exit()
'''

instructions = open("input.txt").read().splitlines()

init_cubes_on = set()
cubes = []
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

	# Separate big cubes from init (small) cubes (they do never overlap):
	if dx * dy * dz == 0:
		cubes.append(Cube(range_x, range_y, range_z, ins.split(" ")[0]))
		continue

	for i in range(range_x[0], range_x[1] + 1):
		for j in range(range_y[0], range_y[1] + 1):
			for k in range(range_z[0], range_z[1] + 1):
				if "off" in ins:
					if (i, j, k) in init_cubes_on:
						init_cubes_on.remove((i, j, k))
				else:
					init_cubes_on.add((i, j, k))

# Init cubes and big cubes do not overlap.
res = []
for cube in cubes:
	if cube.type == "on":
		cur = [cube]
		for already in res:
			nxt = []
			for c in cur:
				nxt.extend(already + c)
			cur = nxt
		res.extend(cur)
	elif cube.type == "off":
		nxt = []
		for already in res:
			nxt.extend(already - cube)
		res = nxt

cubes_on = len(init_cubes_on) + sum([c.cardinality() for c in res])

print(f"Amount of cubes that are on: {cubes_on} ({len(init_cubes_on)} from the initialization procedure region)")
assert cubes_on == 1267133912086024 and len(init_cubes_on) == 607573
