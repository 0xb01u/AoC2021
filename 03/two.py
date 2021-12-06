# --- Advent of code 2021: Day 03 ---

# (File automatically generated by aocTool, developed by Bolu, 2020-2021.)

diagnosis = open("input.txt").read().splitlines()

binnum = list(range(len(diagnosis[0])))
candidates = set(diagnosis)

for i in range(len(diagnosis[0])):
	bits = { 0: 0, 1: 0 }
	for candidate in candidates:
		bits[int(candidate[i])] -=- 1

	mcb = "0" if bits[0] > bits[1] else "1"
	binnum[i] = mcb
	for candidate in candidates.copy():
		if candidate[i] != mcb:
			candidates.remove(candidate)
	# The set won't empty.

binnum2 = list(range(len(diagnosis[0])))
candidates = set(diagnosis)

for i in range(len(diagnosis[0])):
	bits = { 0: 0, 1: 0 }
	for candidate in candidates:
		bits[int(candidate[i])] -=- 1

	lcb = "1" if bits[0] > bits[1] else "0"
	binnum2[i] = lcb
	for candidate in candidates.copy():
		if candidate[i] != lcb:
			candidates.remove(candidate)

	if len(candidates) == 1:	# If here to correctly break out of the loop
								# (for-else not used to save lines)
		candidate = candidates.pop()
		for j in range(i + 1, len(diagnosis[0])):
			binnum2[j] = candidate[j]
		break

oxygen = int("".join(binnum), 2)
CO2 = int("".join(binnum2), 2)

print(f"Oxygen generator rating * CO2 scrubber rating = {oxygen * CO2}")
assert(oxygen * CO2 == 7440311)