-- --- Advent of code 2021: Day 12 ---

-- (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

package.path = package.path .. ";../modules/?.lua"
local tools = require "tools"

caves = tools.readlines("input.txt")

connections = {}
small_caves = {}
for _, cave in pairs(caves) do
	org, dst = table.unpack(tools.split(cave, "-"))
	if not connections[org] then
		connections[org] = {}
	end
	connections[org][dst] = true
	if dst ~= "end" and org ~= "start" then
		if not connections[dst] then
			connections[dst] = {}
		end
		connections[dst][org] = true
	end
	if org:sub(1, 1) >= 'a' then
		small_caves[org] = true
	end
end
small_caves["end"] = nil
small_caves.start = nil

function explore(node, caves, small_caves, explored, path, paths)
	for nxt, _ in pairs(caves[node]) do
		if nxt == "end" then
			paths[#paths + 1] = path .. ",end"
		elseif not explored[nxt] then
			explored_nxt = {}
			for cave, _ in pairs(explored) do
				explored_nxt[cave] = true
			end
			if small_caves[nxt] then
				explored_nxt[nxt] = true
			end
			explore(nxt, caves, small_caves, explored_nxt, path .. "," .. tostring(nxt), paths)
		end
	end
end

paths = {}
explore("start", connections, small_caves, {}, "start", paths)
print("Amount of paths that only visit small caves at least once: " .. #paths)
assert(#paths == 4104)
