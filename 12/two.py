# --- Advent of code 2021: Day 12 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

caves = open("input.txt").read().splitlines()

connections = { cave.split("-")[0]: set() for cave in caves }
for a, b in map(lambda cave: cave.split("-"), caves):
	connections[a].add(b)

small_caves = { cave.split("-")[1] for cave in caves if cave.split("-")[1][0] >= 'a' }
for cave in caves:
	if cave.split("-")[0][0] >= 'a':
		small_caves.add(cave.split("-")[0])
small_caves.remove('end')
small_caves.remove('start')

for a in list(connections.keys()):
	for b in connections[a]:
		if b == 'end':
			continue
		elif b not in connections:
			connections[b] = set()
		if a != 'start':
			connections[b].add(a)

def explore(node, caves, small_caves, explored, path, paths, twice=False):
	for nxt in caves[node]:
		if nxt == 'end':
			paths.append(path + ',end')
		elif nxt not in explored:
			explored_nxt = explored.copy()
			if nxt in small_caves:
				explored_nxt.add(nxt)
			explore(nxt, caves, small_caves, explored_nxt, path + f",{nxt}", paths, twice)
		elif not twice:
			explored_nxt = explored.copy()
			explore(nxt, caves, small_caves, explored_nxt, path + f",{nxt}", paths, True)


paths = []
explore('start', connections, small_caves, set(), 'start', paths)
print(f"Amount of paths that only visit small caves at least once and maybe one twice: {len(paths)}")
assert len(paths) == 119760
