-- --- Advent of code 2021: Day 14 ---

-- (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

package.path = package.path .. ";../modules/?.lua"
local tools = require "tools"

input = tools.readlines("input.txt")

template = input[1]
input[1] = nil
input[2] = nil

rules = {}
for _, rule in pairs(input) do
	a, _, b = table.unpack(tools.split(rule, " "))
	rules[a] = b
end

cont = {}
for i = 1, #template - 1 do
	_, count = string.gsub(template, template:sub(i, i + 1), "")
	cont[template:sub(i, i + 1)] = count
end

for _ = 1, 10 do
	new_cont = {}
	for gen, qty in pairs(cont) do
		char = rules[gen]
		if not new_cont[gen:sub(1, 1) .. char] then
			new_cont[gen:sub(1, 1) .. char] = 0
		end
		new_cont[gen:sub(1, 1) .. char] = new_cont[gen:sub(1, 1) .. char]- -qty
		if not new_cont[char .. gen:sub(2, 2)] then
			new_cont[char .. gen:sub(2, 2)] = 0
		end
		new_cont[char .. gen:sub(2, 2)] = new_cont[char .. gen:sub(2, 2)]- -qty
	end
	cont = new_cont
end

char_cont = {}
char_cont[template:sub(1, 1)] = 1
max_cont = 0
min_cont = 0xffffffff
for gen, count in pairs(cont) do
	if not char_cont[gen[2]] then
		char_cont[gen[2]] = 0
	end
	char_cont[gen[2]] = char_cont[gen[2]]- -count
	if char_cont[gen[2]] > max_cont then
		max_cont = char_cont[gen[2]]
	end
end

for char, count in pairs(char_cont) do
	if count < min_cont then
		min_cont = count
	end
end

score = max_cont - min_cont
print("Quantity of the most common element - quantity of the least common element after 10 steps: " .. score)
assert(score == 2003)
