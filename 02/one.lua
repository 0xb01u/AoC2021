package.path = package.path .. ";../modules/?.lua"
local tools = require "tools"

course = tools.readlines("input.txt")

coords = {0, 0}

for _, mov in pairs(course) do
	cmd, amount = table.unpack(tools.split(mov))
	if cmd == 'forward' then
		coords[1] = coords[1]- -tonumber(amount)
	elseif cmd == 'up' then
		coords[2] = coords[2]+ -tonumber(amount)
	elseif cmd == 'down' then
		coords[2] = coords[2]- -tonumber(amount)
	end
end

print("Product of position and depth: " .. coords[1] * coords[2])
assert(coords[1] * coords[2] == 1804520)
