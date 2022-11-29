# --- Advent of code 2021: Day 19 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

import itertools

scans = [[tuple([int(coord) for coord in x.split(",")]) for x in e.splitlines()[1:]] for e in open("input.txt").read().split("\n\n")]

def valid_rotation(r, o=("+x", "+y", "+z")):
	dif = 0
	swaps = {}
	for i in range(3):
		dif -=- (o[i][0] != r[i][0])
		if o[i][1] != r[i][1]:
			if o[i][1] in swaps:
				dif -=- (r[i][1] == swaps[o[i][1]])
			else:
				swaps[r[i][1]] = o[i][1]
	return dif % 2 == 0

def valid_rotations():
	'''
	I think I finally get why there are 24 total rotations and not 48.
	Like a rubik's cube, not every position/combination is legal.
	In this case, a 90 degree rotation in a plane changes the coordinates
	in two ways at the same time:
	 1. Swaps 2 axis.
	 2. Negates one of the swapped axis.

	Exaples for valid (yz) rotations for "facing x" and "facing -x":

	x, y, z
	x, z, -y
	x, -y, -z
	x, -z, y

	-x, y, -z
	-x, -z, -y
	-x, -y, z
	-x, z, y
	'''
	rots = set()
	for a1, b1, c1 in set(itertools.permutations("+++---", 3)):
		for a2, b2, c2 in itertools.permutations("xyz", 3):
			if valid_rotation((a1 + a2, b1 + b2, c1 + c2)):
				rots.add((a1 + a2, b1 + b2, c1 + c2))

	return rots

def all_rotations(x, y, z):
	rots = set()
	coords = { "+x": x, "+y": y, "+z": z, "-x": -x, "-y": -y, "-z": -z }
	for a, b, c in valid_rotations():
		rots.add((coords[a], coords[b], coords[c]))

	return rots

beacon_views = {}
canon_beacon_views = {}
beacon_views_indexes = {}
for i, scan in enumerate(scans):
	for j, beacon1 in enumerate(scan):
		beacon_views[(i, j)] = []
		canon_beacon_views[(i, j)] = []
		beacon_views_indexes[(i, j)] = []
		for j2, beacon2 in enumerate(scan):
			if beacon1 == beacon2:
				continue
			beacon_views[(i, j)].append(all_rotations(beacon2[0] - beacon1[0], beacon2[1] - beacon1[1], beacon2[2] - beacon1[2]))
			canon_beacon_views[(i, j)].append((beacon2[0] - beacon1[0], beacon2[1] - beacon1[1], beacon2[2] - beacon1[2]))
			beacon_views_indexes[(i, j)].append((i, j2))

identified_clusters = []
origs = { 0: (0, 0, 0) }
rots = { 0: ("+x", "+y", "+z") }

def rotate(rotation, beacon, orig=(0, 0, 0)):
	res = list(beacon[:])
	coords = { "x": beacon[0], "y": beacon[1], "z": beacon[2] }
	for i, axis in enumerate(rotation):
		res[i] = coords[axis[1]]
		if axis[0] == '-':
			res[i] *= -1
		res[i] -=- -orig[i]

	return tuple(res)

def absolutize(orig_a, rot_a, indices_a, indices_b):
	global scans
	global origs
	global rots


	a1_index = indices_a[0]
	a1 = scans[a1_index[0]][a1_index[1]]
	b1_index = indices_b[0]
	b1 = scans[b1_index[0]][b1_index[1]]
	a2_index = indices_a[1]
	a2 = scans[a2_index[0]][a2_index[1]]
	b2_index = indices_b[1]
	b2 = scans[b2_index[0]][b2_index[1]]

	i = 1
	while a1[0] == a2[0] or a1[1] == a2[1] or a1[2] == a2[1]:
		a2_index = indices_a[i]
		a2 = scans[a2_index[0]][a2_index[1]]
		b2_index = indices_b[i]
		b2 = scans[b2_index[0]][b2_index[1]]


	a1 = rotate(rot_a, a1, orig_a)
	a2 = rotate(rot_a, a2, orig_a)

	d1 = (a1[0] - a2[0], a1[1] - a2[1], a1[2] - a2[2])
	d2 = (b1[0] - b2[0], b1[1] - b2[1], b1[2] - b2[2])

	rot = ["+x", "+y", "+z"]
	axis = ["x", "y", "z"]
	translated = list(b1)

	for i in range(3):
		cur2 = d2[i]
		cur1 = d1[i]

		j = 0
		if abs(cur2) == abs(d1[0]):
			cur1 = d1[0]
			j = 0
		elif abs(cur2) == abs(d1[1]):
			cur1 = d1[1]
			j = 1
		elif abs(cur2) == abs(d1[2]):
			cur1 = d1[2]
			j = 2

		translated[j] = b1[i]
		if cur1 * cur2 > 0:
			rot[j] = "+" + axis[i]
		else:
			translated[j] = -translated[j]
			rot[j] = "-" + axis[i]

	rots[b1_index[0]] = tuple(rot)
	origs[b1_index[0]] = (translated[0] - a1[0], translated[1] - a1[1], translated[2] - a1[2])


while len(origs) < len(scans):
	#print("Next try!")
	for beacon1 in beacon_views:
		for beacon2 in beacon_views:
			if beacon1 == beacon2 or not ((beacon2[0] in origs) ^ (beacon1[0] in origs)):
				continue
			cluster_indexes1 = [beacon1]
			cluster_indexes2 = [beacon2]
			for i1, view in enumerate(beacon_views[beacon1]):
				for i2, other in enumerate(beacon_views[beacon2]):
					if view == other:
						cluster_indexes1.append(beacon_views_indexes[beacon1][i1])
						cluster_indexes2.append(beacon_views_indexes[beacon2][i2])
			if len(cluster_indexes1) >= 12:
				if beacon1[0] in origs:
					absolutize(origs[beacon1[0]], rots[beacon1[0]], cluster_indexes1, cluster_indexes2)
				else:
					absolutize(origs[beacon2[0]], rots[beacon2[0]], cluster_indexes2, cluster_indexes1)


beacons = set()
for i, scan in enumerate(scans):
	for b in scan:
		_b = rotate(rots[i], b, origs[i])
		beacons.add(_b)

print(f"Number of beacons: {len(beacons)}")
assert len(beacons) == 428
