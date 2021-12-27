# --- Advent of code 2021: Day 14 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

template, rules = open("input.txt").read().split("\n\n")
rules = { r.split(" -> ")[0]: r.split(" -> ")[1] for r in rules.splitlines() }

for _ in range(10):
	new_template = template[0]
	for i in range(len(template) - 1):
		pair = template[i:i + 2]
		new_template += rules[pair] + pair[1]

	template = new_template

score = template.count(max(template, key=template.count)) - template.count(min(template, key=template.count))
print(f"Quantity of the most common element - quantity of the least common element after 10 steps: {score}")
assert score == 2003
