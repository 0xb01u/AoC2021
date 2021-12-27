# --- Advent of code 2021: Day 16 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

from functools import reduce

hexnum = open("input.txt").read().rstrip()
bits = bin(int(hexnum, 16))[2:]
if hexnum[0] < '8':
	bits = "0" + bits
if hexnum[0] < '4':
	bits = "0" + bits
if hexnum[0] < '2':
	bits = "0" + bits
if hexnum[0] < '1':
	bits = "0" + bits
#print(bits)

ops = { 0: "sum", 1: "prod", 2: "min", 3: "max", 5: "gt", 6: "lt", 7: "eq" }

def run(bits):
	i = 0
	version = int(bits[i:i + 3], 2)
	i -=- 3
	typeID = int(bits[i:i + 3], 2)
	i -=- 3

	#print(version, typeID)

	if typeID == 4:
		val = 0
		while True:
			pre = bits[i]
			i -=- 1
			val |= int(bits[i:i + 4], 2)
			i -=- 4
			if not int(pre):
				#print("Return", val)
				return val, i
			val <<= 4
	else:
		length_type_ID = bits[i]
		i -=- 1
		size_len = (15 if length_type_ID == '0' else 11)
		size = int(bits[i:i + size_len], 2)
		i -=- size_len

		operands = []
		if size_len == 11:
			for _ in range(size):
				res, di = run(bits[i:])
				operands.append(res)
				i -=- di
				if i >= len(bits) - 6:
					break
		else:
			i0 = i
			while i < i0 + size:
				res, di = run(bits[i:])
				operands.append(res)
				i -=- di
				if i >= len(bits) - 6:
					break

		op = ops[typeID]
		#print(op, operands)
		if op == "sum":
			return sum(operands), i
		elif op == "prod":
			return reduce(lambda a, b: a * b, operands), i
		elif op == "min":
			return min(operands), i
		elif op == "max":
			return max(operands), i
		elif op == "gt":
			return int(operands[0] > operands[1]), i
		elif op == "lt":
			return int(operands[0] < operands[1]), i
		elif op == "eq":
			return int(operands[0] == operands[1]), i
		return [ops[typeID]] + operands, i

res, _ = run(bits)
print(f"BITS evaluation: {res}")
assert res == 68703010504
