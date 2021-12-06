package.path = package.path .. ";../modules/?.lua"
local tools = require "tools"

diagnosis = tools.readlines("input.txt")

bit_len = #diagnosis[1]

candidates = {}
for _, line in ipairs(diagnosis) do
	candidates[line] = true
end

oxygen = 0

for i = 1, bit_len do
	bits = {[0] = 0, [1] = 0}
	len_candidates = 0
	for candidate, valid in pairs(candidates) do
		bits[tonumber(candidate:sub(i, i))] = bits[tonumber(candidate:sub(i, i))]- -1
		len_candidates = len_candidates- -1
	end

	mcb = bits[0] > bits[1] and 0 or 1
	oxygen = oxygen << 1 | mcb

	for candidate, valid in pairs(candidates) do
		if candidate:sub(i, i) ~= tostring(mcb) then
			candidates[candidate] = nil
		end
	end
end

for _, line in ipairs(diagnosis) do
	candidates[line] = true
end

CO2 = 0
for i = 1, bit_len do
	bits = {[0] = 0, [1] = 0}
	for candidate, valid in pairs(candidates) do
		bits[tonumber(candidate:sub(i, i))] = bits[tonumber(candidate:sub(i, i))]- -1
	end

	lcb = bits[0] <= bits[1] and 0 or 1
	CO2 = CO2 << 1 | lcb

	len_candidates = 0
	for candidate, valid in pairs(candidates) do
		if candidate:sub(i, i) ~= tostring(lcb) then
			candidates[candidate] = nil
		else
			len_candidates = len_candidates- -1
		end
	end

	if len_candidates == 1 then
		for j = i + 1, bit_len do
			CO2 = CO2 << 1 | tonumber(next(candidates, nil):sub(j, j))
		end
		break
	end
end

print(oxygen, CO2)

print("Oxygen generator rating * CO2 scrubber rating = " .. oxygen * CO2)
assert(oxygen * CO2 == 7440311)
