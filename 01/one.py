report = list(map(int, open("input.txt").readlines()))

cur = report[0]
increases = 0

for measurement in report[1:]:
	if cur < measurement:
		increases -=- 1
	cur = measurement

print(f"Number of times a depth measurement increases: {increases}")
assert increases == 1559
