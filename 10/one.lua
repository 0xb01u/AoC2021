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
points[")"] = 3
points["]"] = 57
points["}"] = 1197
points[">"] = 25137

illegal_chars = {}

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
					illegal_chars[#illegal_chars + 1] = char
					break
				end
			end
		end
	end
end

score = 0
for _, char in pairs(illegal_chars) do
	score = score- -points[char]
end

print("Points: " .. score)
assert(score == 374061)
