# --- Advent of code 2021: Day 23 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

diagram = open("input.txt").read().splitlines()

energy = { "A": 1, "B": 10, "C": 100, "D": 1000 }
rooms = { "A": [(2, 3), (3, 3)], "B": [(2, 5), (3, 5)], "C": [(2, 7), (3, 7)], "D": [(2, 9), (3, 9)] }

walkable = set()
stoppable = set()

pos = {}

for i in range(len(diagram)):
	for j in range(len(diagram[i])):
		if diagram[i][j] == '.':
			walkable.add((i, j))
			if not (diagram[i + 1][j] >= 'A' and diagram[i + 1][j] <= 'D'):
				stoppable.add((i, j))
		if diagram[i][j] >= 'A' and diagram[i][j] <= 'D':
			pos[(i, j)] = diagram[i][j]
			walkable.add((i, j))

class State:
	def __init__(self, pos, energy = 0, moved_once = {}, history = []):
		self.energy = energy
		self.pos = pos.copy()
		self.moved_once = moved_once.copy()
		self.history = history

	def distance(self, a, b):
		return abs(a[0] - b[0]) + abs(a[1] - b[1])

	def explore(self, pos, explored, add = True):
		reachable = []
		if (pos[0] - 1, pos[1]) in walkable and (pos[0] - 1, pos[1]) not in self.pos:
			new_explored = explored.copy()
			new_explored.add((pos[0] - 1, pos[1]))
			reachable.extend(self.explore((pos[0] - 1, pos[1]), new_explored))
		if (pos[0], pos[1] - 1) in walkable and (pos[0], pos[1] - 1) not in self.pos and (pos[0], pos[1] - 1) not in explored:
			new_explored = explored.copy()
			new_explored.add((pos[0], pos[1] - 1))
			reachable.extend(self.explore((pos[0], pos[1] - 1), new_explored))
		if (pos[0], pos[1] + 1) in walkable and (pos[0], pos[1] + 1) not in self.pos and (pos[0], pos[1] + 1) not in explored:
			new_explored = explored.copy()
			new_explored.add((pos[0], pos[1] + 1))
			reachable.extend(self.explore((pos[0], pos[1] + 1), new_explored))
		if pos in stoppable and add:
			reachable.append(pos)

		return reachable

	def valid_movements(self):
		valid = []
		for p, letter in self.pos.items():
			if p in rooms[letter] and letter in self.moved_once and (p in self.moved_once[letter] or p[0] == 3):
				continue

			if letter in self.moved_once and p in self.moved_once[letter]:
				can_enter = True
				for fp in rooms[letter]:
					if fp in self.pos and self.pos[fp] != letter:
						can_enter = False
				for j in range(1, abs(p[1] - rooms[letter][0][1])):
					if (1, min(p[1], rooms[letter][0][1]) + j) in self.pos:
						can_enter = False

				if can_enter:
					for fp in rooms[letter]:
						if fp not in self.pos:
							new_pos = self.pos.copy()
							del new_pos[p]
							new_pos[fp] = letter
							new_moved_once = { k: v[:] for k, v in self.moved_once.items() }
							new_moved_once[letter].remove(p)
							new_moved_once[letter].append(fp)
							valid.append(State(new_pos, self.energy + energy[letter] * self.distance(p, fp), new_moved_once, self.history + [(letter, p, fp, energy[letter] * self.distance(p, fp))]))
							break
			else:
				can_enter = p[0] == 2
				for fp in rooms[letter]:
					if fp in self.pos and self.pos[fp] != letter:
						can_enter = False
				for j in range(abs(p[1] - rooms[letter][0][1])):
					if (1, min(p[1], rooms[letter][0][1]) + j) in self.pos:
						can_enter = False

				if can_enter:
					for fp in rooms[letter]:
						if fp not in self.pos:
							new_pos = self.pos.copy()
							del new_pos[p]
							new_pos[fp] = letter
							new_moved_once = { k: v[:] for k, v in self.moved_once.items() }
							if letter not in new_moved_once:
								new_moved_once[letter] = []
							new_moved_once[letter].append(fp)
							extra_energy = energy[letter] * (p[0] - 1)
							valid.append(State(new_pos, self.energy + energy[letter] * self.distance((1, p[1]), fp) + extra_energy, new_moved_once, self.history + [(letter, p, fp, energy[letter] * self.distance((1, p[1]), fp) + extra_energy)]))
							break
				else:
					valid_pos = self.explore(p, set([p]), False)
					for np in valid_pos:
						new_pos = self.pos.copy()
						del new_pos[p]
						new_pos[np] = letter
						new_moved_once = { k: v[:] for k, v in self.moved_once.items() }
						if letter not in new_moved_once:
							new_moved_once[letter] = []
						new_moved_once[letter].append(np)
						valid.append(State(new_pos, self.energy + energy[letter] * self.distance(p, np), new_moved_once, self.history + [(letter, p, np, energy[letter] * self.distance(p, np))]))
		return valid

	def finished(self):
		fin = True
		for p, letter in self.pos.items():
			if p not in rooms[letter]:
				return False
		return True

	def __hash__(self):
		string = ""
		for i in range(5):
			for j in range(13):
				if (i, j) in walkable:
					if (i, j) in self.pos:
						string += self.pos[(i, j)]
					else:
						string += "."
		return hash(string)

	def __eq__(self, other):
		return self.pos == other.pos

	def __lt__(self, other):
		return self.energy < other.energy

	def __le__(self, other):
		return self.energy <= other.energy

	def __ge__(self, other):
		return self.energy >= other.energy

	def __gt__ (sefl, other):
		return self.energy > other.energy

	def __repr__(self):
		rep = ""
		for i in range(5):
			for j in range(13):
				if (i, j) in self.pos:
					rep += self.pos[(i, j)]
				elif not (i, j) in walkable:
					rep += '#'
				else:
					rep += '.'
			rep += "\n"
		rep += f"Total energy used: {self.energy}\n"
		rep += f"Movenemts: {str(self.history)}\n"
		if (self.finished()):
			rep += "[Finished]\n"

		return rep

states = [State(pos)]
visited = set()
min_energy = 18300	# Trial and error.
moves = 0
while len(states) > 0:
	print(f"Movement: {moves}; states: {len(states)}")
	new_states = []
	for state in states:
		if state.energy > min_energy or state in visited:
			continue
		if state.finished():
			#print(state.history)
			if state.energy < min_energy:
				min_energy = state.energy
				print(f"New minimal energy found: {min_energy}")
		else:
			new_states.extend(state.valid_movements())
		visited.add(state)

	states = sorted(new_states)

	moves -=- 1
	if moves == 0:	# Debug
		[print(state) for state in states]
		exit()

print(f"Least energy required to organize the amphipods: {min_energy}")
assert min_energy == 18195

# Movements to solve the example: [('B', (2, 7), (1, 4), 40), ('C', (2, 5), (2, 7), 400), ('D', (3, 5), (1, 6), 3000), ('B', (1, 4), (3, 5), 30), ('D', (2, 3), (2, 5), 40), ('D', (2, 9), (1, 8), 2000), ('A', (3, 9), (1, 10), 3), ('D', (1, 8), (3, 9), 2000), ('D', (1, 6), (2, 9), 5000), ('A', (1, 10), (2, 3), 8)]
