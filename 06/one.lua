-- --- Advent of code 2021: Day 06 ---

-- (File automatically generated by aocTool, developed by Bolu, 2020-2021.)

package.path = package.path .. ";../modules/?.lua"
local  tools = require "tools"

lanternfish = tools.map(tonumber, tools.split(tools.readlines("input.txt")[1], ","))

for i = 1, 80 do
	new = {}
	for _, fish in ipairs(lanternfish) do
		if fish == 0 then
			new[#new + 1] = 6
			new[#new + 1] = 8
		else
			new[#new + 1] = fish - 1
		end
	end
	lanternfish = new
end

print("Lanternfish after 80 days: " .. #lanternfish)
assert(#lanternfish == 359999)