package.path = package.path .. ";../modules/?.lua"
local tools = require "tools"

diagnosis = tools.readlines("input.txt")

bit_len = #diagnosis[1]
bits = {}
for i = 1, bit_len do
	bits[i] = {[0] = 0, [1] = 0}
end

for _, line in pairs(diagnosis) do
	for i = 1, bit_len do
		bits[i][tonumber(line:sub(i, i))] = bits[i][tonumber(line:sub(i, i))]- -1
	end
end


gamma = 0
for i = 1, bit_len do
	mcb = bits[i][0] > bits[i][1] and 0 or 1
	gamma = gamma << 1 | mcb
end

epsilon = gamma ~ (2^bit_len - 1)

print(gamma, epsilon);

print("Gamma rate * epsilon rate = " .. gamma * epsilon)
assert(gamma * epsilon == 3959450)
