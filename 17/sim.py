target = [[20, 30+1], [-10, -5+1]]

'''
(7, 9)
(6, 8)
(6, 9)
(7, 8)
'''

pos = [0, 0]
step = 0
vel = [7, 9]
y_max = 0
while pos[0] not in range(*target[0]) or pos[1] not in range(*target[1]):
	pos[0] -=- vel[0]
	pos[1] -=- vel[1]
	if vel[0] > 0:
		vel[0] -=- -1
	if vel[0] < 0:
		vel[0] -=- 1
	vel[1] -=- -1
	if pos[1] < target[1][0]:
		print(pos[1])
		break

print(pos)
