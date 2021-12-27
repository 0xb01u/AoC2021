-- --- Advent of code 2021: Day 15 ---

-- (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

package.path = package.path .. ";../modules/?.lua"
local tools = require "tools"

risk = tools.readlines("input.txt")

dest = tostring(#risk) .. "," .. tostring(#risk[1])

dist = {}
Q = {}
for i = 1, #risk do
	for j = 1, #risk[1] do
		dist[tostring(i) .. "," .. tostring(j)] = 0xffffffff
	end
end

dist["1,1"] = 0
Q["1,1"] = true

-- For some reason, this (the Shortest Path Faster Algorithm) is prohibitively
-- slow in Lua (75s for this small case), or at least this implementation of
-- the algorithm.
-- It might have to do with the random ordering Lua gives to the keys in a
-- table.
while tools.size(Q) > 0 do
	u = tools.popkey(Q)
	print(tools.size(Q))

	neighbors = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}}
	for _, neighbor in pairs(neighbors) do
		i, j = table.unpack(tools.map(tonumber, neighbor))
		v1 = tonumber(tools.split(u, ",")[1]) + i
		v2 = tonumber(tools.split(u, ",")[2]) + j
		v_key = tostring(v1) .. "," .. tostring(v2)
		if dist[v_key] and dist[u] + tonumber(risk[v1]:sub(v2, v2)) < dist[v_key] then
			dist[v_key] = dist[u] + tonumber(risk[v1]:sub(v2, v2))
			Q[v_key] = true
		end
	end
end

print("Lowest toal risk: " .. dist[dest])
assert(dist[dest] == 447)
