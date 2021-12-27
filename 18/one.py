# --- Advent of code 2021: Day 18 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

raw_sums = open("input.txt").read().splitlines()

sums = []
for addend in raw_sums:
	depth = -1
	sums.append([])
	for c in addend:
		if c == ',':
			continue
		elif c == '[':
			depth -=- 1
		elif c == ']':
			depth -=- -1
		else:
			sums[-1].append([depth, int(c)])

def add(a, b):
	res = []
	for e in a:
		res.append([e[0] + 1, e[1]])
	for e in b:
		res.append([e[0] + 1, e[1]])
	return res

def explode(l):
	for i in range(len(l)):
		if l[i][0] == 4:
			if i > 0:
				l[i - 1][1] -=- l[i][1]
			if i < len(l) - 2:
				l[i + 2][1] -=- l[i + 1][1]
			l[i] = [3, 0]
			l.pop(i + 1)
			return l, False
	return l, True

from math import ceil

def split(l):
	for i in range(len(l)):
		if l[i][1] >= 10:
			l = l[:i + 1] + [[l[i][0] + 1, ceil(l[i][1] / 2)]] + l[i + 1:]
			l[i][0] -=- 1
			l[i][1] //= 2
			return l, False
	return l, True

def reconstruct(l):
	list4 = []
	list3 = []
	list2 = []
	list1 = []
	list0 = []

	for n in l:
		if len(list4) == 2:
			list3.append(list4)
			list4 = []
		if len(list3) == 2:
			list2.append(list3)
			list3 = []
		if len(list2) == 2:
			list1.append(list2)
			list2 = []
		if len(list1) == 2:
			list0.append(list1)
			list1 = []

		if n[0] == 0:
			list0.append(n[1])
		elif n[0] == 1:
			list1.append(n[1])
		elif n[0] == 2:
			list2.append(n[1])
		elif n[0] == 3:
			list3.append(n[1])
		elif n[0] == 4:
			list4.append(n[1])

		if len(list4) == 2:
			list3.append(list4)
			list4 = []
		if len(list3) == 2:
			list2.append(list3)
			list3 = []
		if len(list2) == 2:
			list1.append(list2)
			list2 = []
		if len(list1) == 2:
			list0.append(list1)
			list1 = []

	return list0

def magnitude(l):
	if isinstance(l[0], int):
		magnitude0 = l[0]
	else:
		magnitude0 = magnitude(l[0])
	if isinstance(l[1], int):
		magnitude1 = l[1]
	else:
		magnitude1 = magnitude(l[1])
	return 3 * magnitude0 + 2 * magnitude1

res = sums.pop(0)
for addend in sums:
	res = add(res, addend)
	reduced = False
	while not reduced:
		res, reduced = explode(res)
		if reduced:
			res, reduced = split(res)

mag = magnitude(reconstruct(res))
print(f"Magnitude of the final sum: {mag}")
assert mag == 3892
