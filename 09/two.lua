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
			low_points[#low_points + 1] = {i, j}
		end
	end
end

basin_sizes = {}
for _, coords in pairs(low_points) do
	to_visit = {}
	x, y = table.unpack(coords)
	to_visit[tostring(x) .. "_" .. tostring(y)] = true
	visited = {}
	while tools.size(to_visit) > 0 do
		i, j = table.unpack(tools.map(tonumber, tools.split(tools.popkey(to_visit), "_")))
		if i > 1 and not visited[tostring(i - 1) .. "_" .. tostring(j)] and heightmap[i - 1]:sub(j, j) ~= '9' then
			to_visit[tostring(i - 1) .. "_" .. tostring(j)] = true
		end
		if j > 1 and not visited[tostring(i) .. "_" .. tostring(j - 1)] and heightmap[i]:sub(j - 1, j - 1) ~= '9' then
			to_visit[tostring(i) .. "_" .. tostring(j - 1)] = true
		end
		if i < #heightmap and not visited[tostring(i + 1) .. "_" .. tostring(j)] and heightmap[i + 1]:sub(j, j) ~= '9' then
			to_visit[tostring(i + 1) .. "_" .. tostring(j)] = true
		end
		if j < #heightmap[i] and not visited[tostring(i) .. "_" .. tostring(j + 1)] and heightmap[i]:sub(j + 1, j + 1) ~= '9' then
			to_visit[tostring(i) .. "_" .. tostring(j + 1)] = true
		end

		visited[tostring(i) .. "_" .. tostring(j)] = true
	end
	basin_sizes[#basin_sizes + 1] = tools.size(visited)
end

table.sort(basin_sizes)
product = tools.product({table.unpack(basin_sizes, #basin_sizes - 2, #basin_sizes)})

print("Product of the size of the 3 largest baisins: " .. product)
assert(product == 1056330)
