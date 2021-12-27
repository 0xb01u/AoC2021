# --- Advent of code 2021: Day 14 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

template, rules = open("input.txt").read().split("\n\n")
rules = { r.split(" -> ")[0]: r.split(" -> ")[1] for r in rules.splitlines() }

cont = { e[0] + e[1]: template.count(e[0] + e[1]) for e in zip(template[:-1], template[1:]) }

for _ in range(40):
	new_cont = {}
	for gen in cont:
		char = rules[gen]
		if gen[0] + char not in new_cont:
			new_cont[gen[0] + char] = 0
		new_cont[gen[0] + char] -=- cont[gen]
		if char + gen[1] not in new_cont:
			new_cont[char + gen[1]] = 0
		new_cont[char + gen[1]] -=- cont[gen]
	cont = new_cont

char_cont = { template[0]: 1}
for gen in cont:
	if gen[1] not in char_cont:
		char_cont[gen[1]] = 0
	char_cont[gen[1]] -=- cont[gen]

print(max(char_cont.values()),min(char_cont.values()))

score = max(char_cont.values()) - min(char_cont.values())
print(f"Quantity of the most common element - quantity of the least common element after 40 steps: {score}")
assert score == 2276644000111
