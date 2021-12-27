-- --- Advent of code 2021: Day 13 ---

-- (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

package.path = package.path .. ";../modules/?.lua"
local tools = require "tools"

input = tools.readlines("input.txt")

dots = {}
folds = {}
reading_folds = false
for _, line in pairs(input)do
	if reading_folds then
		fold = line:sub(#"fold along _")
		folds[#folds + 1] = fold
	else
		if #line == 0 then
			reading_folds = true
		else
			dots[line] = true
		end
	end
end

for _, fold in pairs(folds) do
	axis, coord = table.unpack(tools.split(fold, "="))
	coord = tonumber(coord)

	new_dots = {}
	for dot, _ in pairs(dots) do
		x, y = table.unpack(tools.map(tonumber, tools.split(dot, ",")))

		if axis == "x" then
			if x < coord then
				new_dots[tostring(x) .. "," .. tostring(y)] = true
			elseif x > coord then
				new_dots[tostring((coord - (x % coord)) % coord) .. "," .. tostring(y)] = true
			end
		else
			if y < coord then
				new_dots[tostring(x) .. "," .. tostring(y)] = true
			elseif y > coord then
				new_dots[tostring(x) .. "," .. tostring((coord - (y % coord)) % coord)] = true
			end
		end
	end
	dots = new_dots
end

x = {}
y = {}

for dot, _ in pairs(dots) do
	_x, _y = table.unpack(tools.map(tonumber, tools.split(dot, ",")))
	x[#x + 1] = _x
	y[#y + 1] = _y
end

str = ""
for j = 0, math.max(table.unpack(y)) do
	for i = 0, math.max(table.unpack(x)) do
		if dots[tostring(i) .. "," .. tostring(j)] then
			str = str .. "#"
		else
			str = str .. " "
		end
	end
	str = str .. "\n"
end

print(str)
