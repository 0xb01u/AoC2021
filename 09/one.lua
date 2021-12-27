package.path = package.path .. ";../modules/?.lua"
local tools = require "tools"

heightmap = tools.readlines("input.txt")

low_points = {}
for i = 1, #heightmap do
	for j = 1, #heightmap[i] do
		height = heightmap[i]:sub(j, j)
		low = true
		if i > 1 then
			low = low and height < heightmap[i - 1]:sub(j, j)
		end
		if j > 1 then
			low = low and height < heightmap[i]:sub(j - 1, j - 1)
		end
		if i < #heightmap then
			low = low and height < heightmap[i + 1]:sub(j, j)
		end
		if j < #heightmap then
			low = low and height < heightmap[i]:sub(j + 1, j + 1)
		end

		if low then
			low_points[#low_points + 1] = height
		end
	end
end

sum = #low_points
for _, low in pairs(low_points) do
	sum = sum- -tonumber(low)
end

print("Sum of the risk levels: " .. sum)
assert(sum == 489)
