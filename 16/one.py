# --- Advent of code 2021: Day 16 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

bits = bin(int(open("input.txt").read().rstrip(), 16))[2:]
bits = "0" * ((4 - int(len(bits)) % 4) % 4) + bits

ops = { 0: "sum", 1: "prod", 2: "min", 3: "max", 5: "gt", 6: "lt", 7: "eq" }

i = 0
versions = []
while i < len(bits) - 6:
	version = int(bits[i:i + 3], 2)
	i -=- 3
	versions.append(version)
	typeID = int(bits[i:i + 3], 2)
	i -=- 3

	#print(version, typeID)

	if typeID == 4:
		while True:
			pre = bits[i]
			#print(pre, bits[i + 1:i + 5])
			i -=- 5
			if not int(pre):
				break
	else:
		print(ops[typeID])
		length_type_ID = bits[i]
		i -=- 1
		i -=- (15 if length_type_ID == '0' else 11)
	#print("i", i)

print(f"Sum of version numbers: {sum(versions)}")
assert sum(versions) == 871
