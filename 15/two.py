# --- Advent of code 2021: Day 15 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

risk_ini = open("input.txt").read().splitlines()
risk = [[0] * 5 * len(risk_ini[0]) for i in range(5 * len(risk_ini))]

for i in range(len(risk)):
	for j in range(len(risk[0])):
		risk[i][j] = (int(risk_ini[i % len(risk_ini)][j % len(risk_ini[0])]) + i // len(risk_ini) + j // len(risk_ini[0]))
		if risk[i][j] >= 10:
			risk[i][j] = risk[i][j] % 10 + risk[i][j] // 10

dest = (len(risk) - 1, len(risk[0]) - 1)

# Shortest Path Faster Algorithm: https://en.wikipedia.org/wiki/Shortest_Path_Faster_Algorithm
dist = {}
Q = set()
for i in range(len(risk)):
	for j in range(len(risk[0])):
		dist[(i, j)] = 0xffffffff

dist[(0, 0)] = 0
Q.add((0, 0))

while len(Q) > 0:
	u = Q.pop()

	for i, j in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
		v = (u[0] + i, u[1] + j)
		if v in dist and dist[u] + risk[v[0]][v[1]] < dist[v]:
			dist[v] = dist[u] + risk[v[0]][v[1]]
			Q.add(v)
# Seems like Dijkstra with a priority queue/heap (using heapq) might be a better option.
# Too bad I have no clue about graphs.

print(f"Lowest total risk: {dist[dest]}")	# 49s, ouch!
assert dist[dest] == 2825
