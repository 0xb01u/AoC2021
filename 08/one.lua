package.path = package.path .. ";../modules/?.lua"
local tools = require "tools"

-- Here we use the median.
signals = tools.readlines("input.txt")
pattern = {}
output = {}
for _, signal in pairs(signals) do
	p_o = tools.split(signal, "|")
	p = p_o[1]
	o = p_o[2]
	pattern[#pattern + 1] = tools.split(p, " ")
	output[#output + 1] = tools.split(o, " ")
end

ones_fours_sevens_and_eights = 0
for _, out in pairs(output) do
	for _, digit in pairs(out) do
		if #digit == 2 or #digit == 4 or #digit == 3 or #digit == 7 then
			ones_fours_sevens_and_eights = ones_fours_sevens_and_eights- -1
		end
	end
end

print("Number of times that the digits 1, 4, 7 or 8 appear in the output values: " .. ones_fours_sevens_and_eights)
assert(ones_fours_sevens_and_eights == 264)
