# --- Advent of code 2021: Day 21 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

positions = open("input.txt").read().splitlines()

pos = []

pos.append(int(positions[0][len("Player 1 starting position: "):]) - 1)
pos.append(int(positions[1][len("Player 2 starting position: "):]) - 1)


points = [0, 0]
universes_won = [0, 0]

pos_results = { i: 0 for i in range(3, 10) }
for i in range(1, 4):
	for j in range(1, 4):
		for k in range(1, 4):
			pos_results[i + j + k] -=- 1

''' First solution: recursive, naive-ish, slow
def wins(pos, points, turn, result, quantity):
	global universes_won
	global pos_results

	pos[turn % 2] -=- result
	points[turn % 2] -=- (pos[turn % 2] % 10 + 1)
	if points[turn % 2] >= 21:
		universes_won[turn % 2] -=- quantity
	else:
		for r in pos_results:
			wins(pos[:], points[:], turn + 1, r, quantity * pos_results[r])

for r in pos_results:
	wins(pos[:], points[:], 0, r, pos_results[r])
'''

states = { ((pos[0], points[0]), (pos[1], points[1])): 1 }
while True:
	nxt = {}
	for state in states:
		for r in pos_results:
			p1 = list(state[0])
			p2 = state[1]

			p1[0] = (p1[0] + r) % 10
			p1[1] -=- (p1[0] + 1)
			if p1[1] >= 21:
				universes_won[0] -=- states[state] * pos_results[r]
			else:
				new_state = (tuple(p1), p2)
				if new_state not in nxt:
					nxt[new_state] = 0
				nxt[new_state] -=- states[state] * pos_results[r]

	states = nxt

	nxt = {}
	for state in states:
		for r in pos_results:
			p1 = state[0]
			p2 = list(state[1])

			p2[0] = (p2[0] + r) % 10
			p2[1] -=- (p2[0] + 1)
			if p2[1] >= 21:
				universes_won[1] -=- states[state] * pos_results[r]
			else:
				new_state = (p1, tuple(p2))
				if new_state not in nxt:
					nxt[new_state] = 0
				nxt[new_state] -=- states[state] * pos_results[r]

	states = nxt

	if len(states) == 0:
		break

''' This seems to be a bit more optimized:
while True:
	nxt = {}
	for r, times in pos_results.items():
		for state, quantity in states.items():
			p1_pos, p1_points = state[0]

			p1_pos = (p1_pos + r) % 10
			p1_points -=- (p1_pos + 1)
			if p1_points >= 21:
				universes_won[0] -=- quantity * times
			else:
				new_state = ((p1_pos, p1_points), state[1])
				if new_state not in nxt:
					nxt[new_state] = quantity * times
				else:
					nxt[new_state] -=- quantity * times

	states = nxt

	nxt = {}
	for r, times in pos_results.items():
		for state, quantity in states.items():
			p2_pos, p2_points = state[1]

			p2_pos = (p2_pos + r) % 10
			p2_points -=- (p2_pos + 1)
			if p2_points >= 21:
				universes_won[1] -=- quantity * times
			else:
				new_state = (state[0], (p2_pos, p2_points))
				if new_state not in nxt:
					nxt[new_state] = quantity * times
				else:
					nxt[new_state] -=- quantity * times

	states = nxt

	if len(states) == 0:
		break
'''

#print(universes_won) # [301304993766094, 291924543777199]

print(f"Number of universes_won in which the player that wins in more universes_won wins: {max(universes_won)}")
assert max(universes_won) == 301304993766094
