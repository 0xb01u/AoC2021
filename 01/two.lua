package.path = package.path .. ";../modules/?.lua"
local tools = require "tools"

report = tools.map(tonumber, tools.readlines("input.txt"))

cur = report[1] + report[2] + report[3]
increases = 0

for i = 2, #report - 2 do
	measurement = report[i] + report[i + 1] + report[i + 2]
	if cur < measurement then
		increases = increases- -1
	end
	cur = measurement
end

print("Number of times a depth measurement increases: " .. increases)
assert(increases == 1600)
