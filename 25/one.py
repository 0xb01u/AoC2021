# --- Advent of code 2021: Day 25 ---

# (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

cucumber_map = [list(s) for s in open("input.txt").read().splitlines()]

steps = 0
while True:
	steps -=- 1
	old = [l[:] for l in cucumber_map]

	for i in range(len(cucumber_map)):
		for j in range(len(cucumber_map[i])):
			if old[i][j] == '>' and old[i][(j + 1) % len(old[i])] == '.':
				cucumber_map[i][j] = '.'
				cucumber_map[i][(j + 1) % len(old[i])] = '>'

	old2 = [l[:] for l in cucumber_map]

	for i in range(len(cucumber_map)):
		for j in range(len(cucumber_map[i])):
			if old2[i][j] == 'v' and old2[(i + 1) % len(old2)][j] == '.':
				cucumber_map[i][j] = '.'
				cucumber_map[(i + 1) % len(old)][j] = 'v'

	if all([old[i] == cucumber_map[i] for i in range(len(cucumber_map))]):
		break

print(f"Steps until all cucumbers stop moving: {steps}")
assert steps == 417

'''
You use all fifty stars to boost the signal and remotely start the sleigh! Now, you just have to find your way back to the surface...

...did you know crab submarines come with colored lights?

Congratulations! You've finished every puzzle in Advent of Code 2021! I hope you had as much fun solving them as I had making them for you. I'd love to hear about your adventure; you can get in touch with me via contact info on my website or through Twitter.

If you'd like to see more things like this in the future, please consider supporting Advent of Code and sharing it with others.

To hear about future projects, you can follow me on Twitter.

I've highlighted the easter eggs in each puzzle, just in case you missed any. Hover your mouse over them, and the easter egg will appear.

You can [Share] this moment with your friends, or [Go Check on Your Calendar].
'''
