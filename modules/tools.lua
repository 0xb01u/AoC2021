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
	if #sep > 1 then error("Split function can only take one-character separators") end
	if sep == nil then sep = "%s" end
	local r = {}
	for s in string.gmatch(str, "([^" .. sep .. "]+)") do
		table.insert(r, s)
	end
	return r
end

--[[ 
-- Better string splitter (Norman Ramsey, https://stackoverflow.com/questions/1426954/split-string-in-lua)
function string:split(pat)
  pat = pat or '%s+'
  local st, g = 1, self:gmatch("()("..pat..")")
  local function getter(segs, seps, sep, cap1, ...)
    st = sep and seps + #sep
    return self:sub(segs, (seps or 0) - 1), cap1 or sep, ...
  end
  return function() if st then return getter(st, g()) end end
end
--]]

local string_meta = getmetatable('')

function string_meta:__index(key)
	local val = string[key]	-- String functions are also accessed by "__index" (e.g: sub function).
	if val then return val end -- These two lines are so lua still finds the builtin functions
	if tonumber(key) then return self:sub(key, key) end
	error("Cannot access index '" .. tostring(key) .. "'' of the string.")
end

return luatools
