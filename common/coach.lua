-- Finds shorter ways to do what you did: the fewest keys that take the cursor where you took it, and one
-- command for an edit you made in several. session.lua runs it after check.py has replayed your keys, and
-- check.py prints what it finds after your try. You never need to edit (or read) this.

local api = vim.api
local M = {}

-- What the coach may suggest, each with the project that teaches it: it never suggests a command you
-- haven't learned yet.
local SINGLE = {
  { "h", 0 }, { "j", 0 }, { "k", 0 }, { "l", 0 }, { "w", 0 }, { "b", 0 }, { "e", 0 },
  { "W", 1 }, { "B", 1 }, { "E", 1 }, { "0", 1 }, { "^", 1 }, { "$", 1 }, { "gg", 1 }, { "G", 1 },
  { "+", 1 }, { "-", 1 }, { "{", 1 }, { "}", 1 }, { "%", 1 }, { "*", 1 }, { "#", 1 }, { "ge", 1 }, { "gE", 1 },
}
local COUNTED = { -- these also get counts 2 to 9
  { "w", 0 }, { "b", 0 }, { "e", 0 }, { "j", 0 }, { "k", 0 }, { "W", 1 }, { "B", 1 }, { "E", 1 },
  { "{", 1 }, { "}", 1 }, { "ge", 1 }, { "gE", 1 },
}
local OBJECTS = { -- text objects, from Project 02
  "iw", "aw", "iW", "aW", "is", "as", "ip", "ap", "i(", "a(", "i{", "a{", "i[", "a[", "i<", "a<",
  "it", "at", 'i"', 'a"', "i'", "a'", "i`", "a`", "2i(", "2a(", "2i{", "2a{",
}

-- A command that starts with one of these keys (after any count) only moves the cursor.
local MOTION_KEYS = {}
for _, k in ipairs({ "h", "j", "k", "l", "w", "b", "e", "W", "B", "E", "0", "^", "$", "G", "+", "-", "_",
  "{", "}", "(", ")", "%", "*", "#", "n", "N", "f", "F", "t", "T", ";", ",", "/", "?", "H", "M", "L", "|",
  "`", "'", "<CR>", "<BS>", "<SPACE>", "<LEFT>", "<RIGHT>", "<UP>", "<DOWN>", "<HOME>", "<END>", "<ESC>",
  "<C-O>", "<C-I>", "<TAB>" }) do
  MOTION_KEYS[k] = true
end
local G_MOTIONS = { g = true, e = true, E = true, _ = true, j = true, k = true, m = true, M = true,
  ["0"] = true, ["^"] = true, ["$"] = true }

local function norm(k) return k:match("^<.+>$") and k:upper() or k end

-- The key that says what a command is: its first after any count, with g's second key ("gn").
local function head(keys)
  local i = 1
  while keys[i] and keys[i]:match("^%d$") and not (i == 1 and keys[i] == "0") do i = i + 1 end
  local k = keys[i]
  if k == "g" then return "g" .. (keys[i + 1] or "") end
  return k and norm(k) or ""
end

local function is_motion(keys)
  local h = head(keys)
  if h:sub(1, 1) == "g" and #h > 1 then return G_MOTIONS[h:sub(2)] or false end
  return MOTION_KEYS[h] or false
end

-- ---------- the state before each key ----------

local snaps = {} -- the text, by signature, for every version of the file you made

function M.state(sig, lines)
  if not snaps[sig] then snaps[sig] = lines() end
  local v = vim.fn.winsaveview()
  return { mode = api.nvim_get_mode().mode, recording = vim.fn.reg_recording() ~= "",
    view = { v.lnum, v.col, v.curswant }, win = api.nvim_get_current_win(), sig = sig }
end

-- Which keys start a new command: those that arrive in Normal mode with nothing pending. Neovim's mode
-- covers operators (d waits in operator-pending mode), Insert, Visual and the command line; what's left
-- to follow is a count, a register ("a), and the keys that take one more key (fx, ma, gU, Ctrl-w j...).
local TAKES_ONE = {}
for _, k in ipairs({ "f", "F", "t", "T", "r", "m", "`", "'", "@", "g", "z", "Z", "[", "]", "<C-W>" }) do
  TAKES_ONE[k] = true
end

local function command_starts(keys, st)
  local starts, expect = {}, "command" -- or "more" (after a count or register) or "char" (fx) or "register"
  for i, key in ipairs(keys) do
    local k = norm(key)
    if st[i] and st[i].mode == "n" then
      starts[i] = expect == "command"
      if expect == "char" then
        expect = "command"
      elseif expect == "register" then
        expect = "more"
      elseif k:match("^[1-9]$") or (k == "0" and expect == "more" and keys[i - 1]:match("^%d$")) then
        expect = "more"
      elseif k == '"' then
        expect = "register"
      elseif TAKES_ONE[k] or (k == "q" and not st[i].recording) then
        expect = "char"
      else
        expect = "command"
      end
    elseif st[i] then
      expect = "command" -- an operator, Insert mode, Visual mode or a command line: back in Normal mode, a new one
    end
  end
  starts[#keys + 1] = expect == "command" and st[#keys + 1] and st[#keys + 1].mode == "n"
  return starts
end

-- ---------- trying keys ----------

local function go(view) vim.fn.winrestview({ lnum = view[1], col = view[2], curswant = view[3] }) end
local function here() local v = vim.fn.winsaveview(); return { v.lnum, v.col, v.curswant } end
local function run(keys) vim.cmd("silent! keepjumps normal! " .. keys) end
local function cost(keys) return vim.fn.strchars(keys) end
local function line(l) return api.nvim_buf_get_lines(0, l - 1, l, true)[1] or "" end
local function set_text(lines) api.nvim_buf_set_lines(0, 0, -1, false, lines) end

-- f, F, t and T to the characters on the line, up to the third of each in that direction.
local function finds(view, add)
  local text, col = line(view[1]), view[2]
  local ahead, behind = {}, {}
  local b = 0
  for ch in text:gmatch("[%z\1-\127\194-\244][\128-\191]*") do
    if #ch > 1 then -- not on the keyboard: f would need a digraph after it, so leave it out
    elseif b > col then
      ahead[ch] = (ahead[ch] or 0) + 1
      if ahead[ch] <= 3 then
        local n = ahead[ch] > 1 and tostring(ahead[ch]) or ""
        add(n .. "f" .. ch, 0); add(n .. "t" .. ch, 0)
      end
    elseif b < col then
      behind[#behind + 1] = ch
    end
    b = b + #ch
  end
  local seen = {}
  for i = #behind, 1, -1 do
    local ch = behind[i]
    seen[ch] = (seen[ch] or 0) + 1
    if seen[ch] <= 3 then
      local n = seen[ch] > 1 and tostring(seen[ch]) or ""
      add(n .. "F" .. ch, 0); add(n .. "T" .. ch, 0)
    end
  end
end

-- Searches for the text at goal: /pat<CR> and ?pat<CR>, patterns 1 to 4 characters long.
local function searches(goal, add)
  local rest = line(goal[1]):sub(goal[2] + 1)
  for len = 1, math.min(4, #rest) do
    local pat = rest:sub(1, len)
    if pat:match("^[%w%p ]+$") then
      add("/" .. vim.fn.escape(pat, "\\/.*$^~[") .. "\r", 1)
      add("?" .. vim.fn.escape(pat, "\\?.*$^~[") .. "\r", 1)
    end
  end
end

-- Every motion worth trying from view, toward goal, for someone who has learned up to project level.
local function motions(view, goal, level, no_search)
  local out = {}
  local function add(k, lvl) if lvl <= level then out[#out + 1] = k end end
  for _, m in ipairs(SINGLE) do
    if not (no_search and (m[1] == "*" or m[1] == "#")) then add(m[1], m[2]) end
  end
  for _, m in ipairs(COUNTED) do
    for n = 2, 9 do add(n .. m[1], m[2]) end
  end
  local dl = goal[1] - view[1]
  if dl > 9 then add(dl .. "j", 0) elseif dl < -9 then add(-dl .. "k", 0) end
  if dl ~= 0 then add(goal[1] .. "G", 1) end
  if dl == 0 then
    for n = 2, 9 do add(n .. "h", 0); add(n .. "l", 0) end
    finds(view, add)
  end
  if not no_search then searches(goal, add) end
  return out
end

-- The fewest keys from view to goal (a line and column), if it takes at most limit keys: cheapest first,
-- so the first path that arrives is a shortest one.
local function shortest(from, goal, limit, level, no_search, deadline)
  local function key(v) return v[1] .. ":" .. v[2] .. ":" .. v[3] end
  local best, buckets = { [key(from)] = 0 }, { [0] = { { from, "" } } }
  for c = 0, limit do
    for _, item in ipairs(buckets[c] or {}) do
      local v, path = item[1], item[2]
      if best[key(v)] == c then
        if c > 0 and v[1] == goal[1] and v[2] == goal[2] then return path end
        if vim.uv.hrtime() > deadline then return nil end
        for _, m in ipairs(motions(v, goal, level, no_search)) do
          local c2 = c + cost(m)
          if c2 <= limit then
            go(v)
            run(m)
            local n = here()
            local k = key(n)
            if not best[k] or c2 < best[k] then
              best[k] = c2
              buckets[c2] = buckets[c2] or {}
              table.insert(buckets[c2], { n, path .. m })
            end
          end
        end
      end
    end
  end
end

-- Text as you'd type it: a character that isn't on the keyboard (é, ×, ≠) goes in as its digraph,
-- Ctrl-k and two keys. nil if one has no digraph.
local digraphs
local function as_typed(text)
  if not digraphs then
    digraphs = {}
    for _, d in ipairs(vim.fn.digraph_getlist(true)) do
      if not digraphs[d[2]] then digraphs[d[2]] = d[1] end
    end
  end
  local out, ok = {}, true
  for ch in text:gmatch("[%z\1-\127\194-\244][\128-\191]*") do
    if #ch == 1 then
      out[#out + 1] = ch
    elseif digraphs[ch] then
      out[#out + 1] = "\v" .. digraphs[ch]
    else
      ok = false
    end
  end
  return ok and table.concat(out) or nil
end

-- The (line, column) of a byte offset in text joined with "\n".
local function position(text, offset)
  local before = text:sub(1, offset)
  local lnum = select(2, before:gsub("\n", "")) + 1
  return { lnum, offset - (before:match(".*\n()") or 1) + 1 }
end

-- One command that turns before into after, starting from view, in fewer than limit keys.
local function one_command(before, view, after, goal_view, limit, level, final)
  local a, b = table.concat(before, "\n"), table.concat(after, "\n")
  local p = 0
  while p < #a and p < #b and a:byte(p + 1) == b:byte(p + 1) do p = p + 1 end
  local s = 0
  while s < #a - p and s < #b - p and a:byte(#a - s) == b:byte(#b - s) do s = s + 1 end
  local function inside(str, i) local c = str:byte(i); return c and c >= 0x80 and c < 0xC0 end
  while p > 0 and (inside(a, p + 1) or inside(b, p + 1)) do p = p - 1 end -- whole characters only
  while s > 0 and inside(a, #a - s + 1) do s = s - 1 end
  local deleted, inserted = a:sub(p + 1, #a - s), b:sub(p + 1, #b - s)
  set_text(before)
  local list = {}
  local function add(k, lvl) if lvl <= level then list[#list + 1] = k end end
  local mots = motions(view, position(a, p + #deleted), level, false)
  if inserted == "" then
    for n = 1, 9 do
      local c = n > 1 and tostring(n) or ""
      add(c .. "x", 0); add(c .. "X", 0); add(c .. "dd", 0)
      if n > 1 then add(c .. "J", 0) end
    end
    add("D", 0)
    for _, m in ipairs(mots) do add("d" .. m, 0) end
    for _, o in ipairs(OBJECTS) do add("d" .. o, 2) end
  elseif as_typed(inserted) then
    local typed = as_typed(inserted):gsub("\n", "\r")
    local tails = { typed .. "\27" }
    local bare = typed:gsub("\r[ \t]+", "\r") -- let autoindent type the indentation
    if bare ~= typed then tails[2] = bare .. "\27" end
    for _, t in ipairs(tails) do
      if deleted == "" then
        for _, c in ipairs({ "i", "a", "I", "A", "o", "O" }) do add(c .. t, 0) end
      end
      for n = 1, 9 do add((n > 1 and tostring(n) or "") .. "s" .. t, 0) end
      for _, c in ipairs({ "S", "C", "cc", "R" }) do add(c .. t, 0) end
      for _, m in ipairs(mots) do add("c" .. m .. t, 0) end
      for _, o in ipairs(OBJECTS) do add("c" .. o .. t, 2) end
    end
    if vim.fn.strchars(inserted) == 1 and vim.fn.strchars(deleted) == 1 then add("r" .. as_typed(inserted), 0) end
  end
  local function price(k) return cost(k) - ((final and k:sub(-1) == "\27") and 1 or 0) end
  table.sort(list, function(x, y) return price(x) < price(y) end)
  for _, k in ipairs(list) do
    if price(k) >= limit then break end
    set_text(before)
    go(view)
    run(k)
    local v = here()
    if table.concat(api.nvim_buf_get_lines(0, 0, -1, false), "\n") == b
        and (final or (v[1] == goal_view[1] and v[2] == goal_view[2])) then
      return k, price(k), deleted, inserted
    end
  end
end

-- ---------- the analysis ----------

local function short(s)
  s = s:gsub("\n", "⏎")
  return vim.fn.strchars(s) > 24 and vim.fn.strcharpart(s, 0, 23) .. "…" or s
end

-- log: one entry per key, { key = "w", st = the state just before it }; final: the state after the last;
-- win: your file's window. Returns what it found: { { kind, from, to (key positions), line, yours, better,
-- saves, note }, ... }
function M.analyze(log, final, level, budget_ms, win)
  return api.nvim_win_call(win, function() return M._analyze(log, final, level, budget_ms, win) end)
end

function M._analyze(log, final, level, budget_ms, win)
  local deadline = vim.uv.hrtime() + budget_ms * 1e6
  vim.bo.undolevels = -1
  local keys, st = {}, {}
  for i, e in ipairs(log) do keys[i], st[i] = e.key, e.st end
  st[#keys + 1] = final
  -- Split the keys into commands.
  local starts = command_starts(keys, st)
  local function idle(i) return starts[i] end
  local cmds, start = {}, 1
  for i = 2, #keys + 1 do
    if i == #keys + 1 or idle(i) then
      local c = { from = start, to = i, keys = vim.list_slice(keys, start, i - 1) }
      local a, b = st[start], st[i]
      c.changed = a.sig ~= b.sig
      c.motion = not c.changed and idle(i) and a.win == b.win and is_motion(c.keys)
      cmds[#cmds + 1] = c
      start = i
    end
  end
  -- Runs of motions, and runs of edits made one right after another.
  local groups = {}
  for _, c in ipairs(cmds) do
    local kind = c.motion and "move" or c.changed and "edit" or nil
    local last = groups[#groups]
    if kind and last and last.kind == kind and last.to == c.from then
      last.to = c.to
    else
      groups[#groups + 1] = { kind = kind, from = c.from, to = c.to }
    end
  end
  -- What the commands after a group start with, and whether any later key is Ctrl-r (in Insert mode or
  -- on the command line it reads a register): replacing keys that these depend on could change them.
  local function after(g)
    local heads, ctrl_r = {}, false
    for _, c in ipairs(cmds) do
      if c.from >= g.to then
        heads[head(c.keys)] = true
        for _, k in ipairs(c.keys) do ctrl_r = ctrl_r or norm(k) == "<C-R>" end
      end
    end
    return heads, ctrl_r
  end
  local function any(set, list)
    for _, k in ipairs(list) do if set[k] then return true end end
  end
  local found, starts = {}, {} -- starts: where an edit can start instead, if the move before it isn't needed
  for gi, g in ipairs(groups) do
    local a, b = st[g.from], st[g.to]
    local spent = g.to - g.from
    if g.to == #keys + 1 and norm(keys[#keys]) == "<ESC>" then spent = spent - 1 end -- a last <Esc> is free
    local mine = table.concat(vim.list_slice(keys, g.from, g.to - 1))
    local heads, ctrl_r = after(g)
    if a.win ~= win then -- in another window: its cursor isn't in your file
    elseif g.kind == "move" and idle(g.from) and snaps[a.sig] then
      local mine_heads = {}
      for _, c in ipairs(cmds) do
        if c.from >= g.from and c.to <= g.to then mine_heads[head(c.keys)] = true end
      end
      local searched = any(mine_heads, { "/", "?", "*", "#", "n", "N" })
      local needs_search = ctrl_r or any(heads, { "n", "N", "&", "gn", "gN", ":" })
      local needs_jumps = any(heads, { "<C-O>", "<C-I>", "<TAB>", "`", "'" })
      if not (searched and needs_search) and not needs_jumps then
        set_text(snaps[a.sig])
        local path, note
        -- Does the edit right after this work just as well from where the move started (A, I, o, dd...)?
        local e = groups[gi + 1]
        if e and e.kind == "edit" and snaps[st[e.to].sig] then
          local final = e.to == #keys + 1
          go(a.view)
          run(api.nvim_replace_termcodes(table.concat(vim.list_slice(keys, e.from, e.to - 1)), true, true, true))
          local v = here()
          if table.concat(api.nvim_buf_get_lines(0, 0, -1, false), "\n") == table.concat(snaps[st[e.to].sig], "\n")
              and (final or (v[1] == st[e.to].view[1] and v[2] == st[e.to].view[2])) then
            path, note, starts[gi + 1] = "", "the edit after it does the same from where you were", a.view
          end
          set_text(snaps[a.sig])
        end
        if path then
        elseif a.view[1] == b.view[1] and a.view[2] == b.view[2] then
          path = ""
        elseif spent > 1 then
          path = shortest(a.view, b.view, spent - 1, level, needs_search, deadline)
        end
        if path and spent - cost(path) > 0 then
          found[#found + 1] = { kind = "move", from = g.from, to = g.to, line = b.view[1], yours = mine,
            better = vim.fn.keytrans(path), saves = spent - cost(path), note = note }
        end
      end
    elseif g.kind == "edit" and spent > 1 and idle(g.from) and snaps[a.sig] and snaps[b.sig] then
      local nxt
      for j = gi + 1, #groups do
        if groups[j].kind == "edit" then nxt = groups[j]; break end
      end
      local dotted = nxt and head(vim.list_slice(keys, nxt.from, nxt.to - 1)) == "."
      local registers = ctrl_r or any(heads, { "p", "P", '"', "@" })
      if not dotted and not registers then
        local k, price, deleted, inserted = one_command(snaps[a.sig], starts[gi] or a.view, snaps[b.sig], b.view,
          spent, level, g.to == #keys + 1)
        if k and vim.fn.keytrans(k) ~= mine then
          local note = inserted == "" and ('deletes "' .. short(deleted) .. '"')
            or deleted == "" and ('types "' .. short(inserted) .. '"')
            or ('"' .. short(deleted) .. '" → "' .. short(inserted) .. '"')
          found[#found + 1] = { kind = "edit", from = g.from, to = g.to, line = a.view[1], yours = mine,
            better = vim.fn.keytrans(k), saves = spent - price, note = note }
        end
      end
    end
    if vim.uv.hrtime() > deadline then break end
  end
  return found
end

return M
