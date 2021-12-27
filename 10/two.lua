-- --- Advent of code 2021: Day 10 ---

-- (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

package.path = package.path .. ";../modules/?.lua"
local tools = require "tools"

lines = tools.readlines("input.txt")

open_chars = {}
open_chars["("] = true
open_chars["{"] = true
open_chars["["] = true
open_chars["<"] = true

correspondence = {}
correspondence["("] = ")"
correspondence["{"] = "}"
correspondence["["] = "]"
correspondence["<"] = ">"

points = {}
points[")"] = 1
points["]"] = 2
points["}"] = 3
points[">"] = 4

incomplete_lines = {}
scores = {}

for _, line in pairs(lines) do
	stack = {}
	for i = 1, #line do
		char = line:sub(i, i)
		if open_chars[char] then
			stack[#stack + 1] = char
		else
			if #stack ~= 0 then
				corresponding = stack[#stack]
				stack[#stack] = nil
				if char ~= correspondence[corresponding] then
					stack = {}
					break
				end
			end
		end
	end
	if #stack ~= 0 then
		scores[#scores + 1] = 0
		for i = 0, #stack - 1  do
			scores[#scores] = scores[#scores] * 5 + points[correspondence[stack[#stack - i]]]
		end
	end
end

table.sort(scores)

print("Middle score: " .. scores[math.ceil(#scores / 2)])
assert(scores[math.ceil(#scores / 2)] == 2116639949)
