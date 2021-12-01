package.path = package.path .. ";../modules/?.lua"
local  tools = require "tools"

report = tools.map(tonumber, tools.readlines("input.txt"))

cur = report[1]
increases = 0

for _, measurement in pairs({table.unpack(report, 2, #report)}) do
	if cur < measurement then
		increases = increases- -1
	end
	cur = measurement
end

print("Number of times a depth measurement increases: " .. increases)
assert(increases == 1559)
