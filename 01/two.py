report = list(map(int, open("input.txt").readlines()))
report3 = list(map(lambda x: x[0] + x[1] + x[2], zip(report[:-2], report[1:-1], report[2:])))

cur = report3[0]
increases = 0

for measurement in report3[1:]:
	if cur < measurement:
		increases -=- 1
	cur = measurement

print(f"Number of times a depth measurement increases: {increases}")
assert increases == 1600
