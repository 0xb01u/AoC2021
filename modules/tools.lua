local luatools = {}

function luatools.map(f, t)
	local t2 = {}
	for k, v in ipairs(t) do t2[k] = f(v) end
	return t2
end

function luatools.reduce(f, t)
	local r = 0
	for k, v in ipairs(t) do r = r + f(v) end
	return r
end

function luatools.file_exists(file)
	local f = io.open(file, "rb")
	if f then f:close() end
	return f ~= nil
end

function luatools.readlines(file)
	if not luatools.file_exists(file) then return {} end
	lines = {}
	for line in io.lines(file) do 
		lines[#lines + 1] = line
	end
	return lines
end

function luatools.split(str, sep)
	if sep == nil then sep = "%s" end
	local r = {}
	for s in string.gmatch(str, "([^" .. sep .. "]+)") do
		table.insert(r, s)
	end
	return r
end

return luatools
