-- --- Advent of code 2021: Day 11 ---

-- (Skeleton file automatically created by aocTool, developed by Bolu, 2020-2021.)

package.path = package.path .. ";../modules/?.lua"
local tools = require "tools"

energy_lines = tools.readlines("input.txt")

energy = {}
for i, line in ipairs(energy_lines) do
	energy[#energy + 1] = {}
	for j = 1, #line do
		energy[i][j] = tonumber(line:sub(j, j))
	end
end

synced = false
step = 1
while true do
	second_step = false
	-- 1
	for i = 1, 10 do
		for j = 1, 10 do
			energy[i][j] = energy[i][j] + 1
			if energy[i][j] > 9 then
				second_step = true
			end
		end
	end

	-- 2
	while second_step do
		second_step = false
		for i = 1, 10 do
			for j = 1, 10 do
				if energy[i][j] > 9 then
					for di = -1, 1 do
						for dj = -1, 1 do
							if i + di > 0 and i + di <= 10 and j + dj > 0 and j + dj <= 10 and (di ~= 0 or dj ~= 0) then
								energy[i + di][j + dj] = energy[i + di][j + dj]- -1
								if energy[i + di][j + dj] > 9 and (di < 0 or dj < 0) then
									second_step = true
								end
							end
						end
					end
					energy[i][j] = -energy[i][j]
				end
			end
		end
	end

	-- 3 and synchronization
	synced = true
	for i = 1, 10 do
		for j = 1, 10 do
			if energy[i][j] < 0 then
				energy[i][j] = 0
			end
			if energy[i][j] ~= 0 then
				synced = false
			end
		end
	end
	if synced then
		break
	end

	step = step- -1
end

print("First synchronization on step: " .. step)
assert(step == 258)
