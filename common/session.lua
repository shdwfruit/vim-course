-- Runs inside Neovim during an exercise: lays out the windows, counts your keys, and records the
-- result for check.py. Started by common/trainer.py. You never need to edit (or read) this.

local api = vim.api
local S = vim.json.decode(table.concat(vim.fn.readfile(vim.env.VIMCOURSE_SESSION), "\n"))
-- Use the paths as Neovim names its buffers (macOS folders are case-insensitive: ~/School is ~/school).
for _, f in ipairs(S.files) do f.path = vim.uv.fs_realpath(f.path) or f.path end
local M = {}
_G.VimCourse = M

local log = {} -- one entry per key you typed: { key = "<Esc>", changed = true/false }
local last_sig -- the exercise text just before the most recent key arrived
local final -- snapshot of the exercise text, taken when you quit
local paused = false -- true while F5 restores the starting state
local done = false -- watch mode: the replay has finished
local leaving -- F7, F8, F9: "prev", "menu" or "next", to leave without grading
local work_win
-- When check.py replays your keys to look for shorter ways to do the same (common/coach.lua)
local coach = S.analyze and dofile(S.analyze.coach)
local coached -- what it found

-- Keys that never count: F1 (command notes), F5 (restart), F7-F9 (leave), and events that aren't really keys.
local function ignored(k)
  return k == "<F1>" or k == "<F5>" or k == "<F7>" or k == "<F8>" or k == "<F9>" or k == "<Ignore>" or k == "<Cmd>" or k:match("^<Focus") or k:match("ScrollWheel")
    or k:match("MouseMove") or k:match("Release>$") or k:match("Drag>$")
    or (k:match("Mouse>$") and not k:match("LeftMouse>$"))
end

-- "ci\"x<Esc>" -> { "c", "i", "\"", "x", "<Esc>" }. A literal "<" becomes "<lt>".
local function split_keys(s)
  local keys, i = {}, 1
  while i <= #s do
    local special = s:match("^<[^<>]+>", i)
    if special and api.nvim_replace_termcodes(special, true, true, true) ~= special then
      keys[#keys + 1] = special
      i = i + #special
    else
      local ch = s:match("^[%z\1-\127\194-\244][\128-\191]*", i)
      keys[#keys + 1] = ch == "<" and "<lt>" or ch
      i = i + #ch
    end
  end
  return keys
end

local function find_buf(path)
  for _, b in ipairs(api.nvim_list_bufs()) do
    if api.nvim_buf_get_name(b) == path then return b end
  end
end

local function file_lines(f)
  local b = find_buf(f.path)
  if b and api.nvim_buf_is_loaded(b) then return api.nvim_buf_get_lines(b, 0, -1, false) end
  if vim.fn.filereadable(f.path) == 1 then return vim.fn.readfile(f.path) end
  return {}
end

local function signature()
  local parts = {}
  for i, f in ipairs(S.files) do parts[i] = table.concat(file_lines(f), "\n") end
  return table.concat(parts, "\0")
end

-- ---------- counting keys ----------
-- A key "changed" the text if the text differs between its arrival and the next key's arrival.
-- Your score is the position of the last key that changed the text, so saving, quitting, and
-- looking around afterwards are free.

vim.on_key(function(_, typed)
  if paused or done or typed == nil or typed == "" then return end
  local keys = vim.tbl_filter(function(k) return not ignored(k) end, split_keys(vim.fn.keytrans(typed)))
  if #keys == 0 then return end
  local sig = signature()
  if #log > 0 and sig ~= last_sig then log[#log].changed = true end
  last_sig = sig
  final = nil -- an earlier quit attempt's snapshot is out of date now
  local st = coach and coach.state(sig, function() return file_lines(S.files[1]) end)
  local mode = api.nvim_get_mode().mode -- for stats.py: which keys were commands and which were typed text
  for i, k in ipairs(keys) do log[#log + 1] = { key = k, changed = false, st = i == 1 and st or nil, mode = mode } end
  vim.schedule(function() pcall(vim.cmd, "redrawstatus!") end)
end)

local function snapshot()
  local files = {}
  for i, f in ipairs(S.files) do files[i] = file_lines(f) end
  final = { sig = signature(), files = files }
end

local function write_result()
  if leaving then
    vim.fn.writefile({ vim.json.encode({ leave = leaving }) }, S.result)
    return
  end
  if not final then pcall(snapshot) end
  if not final then return end
  if #log > 0 and final.sig ~= last_sig then log[#log].changed = true end
  local keys, modes, count = {}, {}, 0
  for i, e in ipairs(log) do
    keys[i], modes[i] = e.key, e.mode
    if e.changed then count = i end
  end
  vim.fn.writefile({ vim.json.encode({ keys = keys, modes = modes, count = count, files = final.files,
    coach = coached }) }, S.result)
end

-- ---------- the window bar ----------

local function esc(s) return (s:gsub("%%", "%%%%")) end

function M.winbar()
  if S.mode == "watch" then
    local typed = {}
    for i, e in ipairs(log) do typed[i] = e.key end
    local shown = table.concat(typed)
    if #shown > 50 then shown = "…" .. shown:sub(-50) end
    local status = done and "%#DiagnosticOk#done · ZZ to exit%*" or "%#DiagnosticInfo#replaying%*"
    return string.format(" %s %%=%%#Comment#%s%%* ", status, esc(shown))
  end
  local color = #log <= S.par and "DiagnosticOk" or "DiagnosticWarn"
  return string.format(" %%#Comment#your file%%*%%=%%#%s#keys %d%%* · par %d ", color, #log, S.par)
end

-- ---------- F5: start over ----------
-- F5 puts back everything an earlier attempt could leave behind, as it was when the exercise started:
-- the text and its undo history, registers, marks, jumps, the search, command history, the argument and
-- quickfix lists, extra buffers, the alternate file, and what ., &, ; and @: would repeat.

local REGISTERS = vim.split('"0123456789abcdefghijklmnopqrstuvwxyz-/', "")
local HISTORIES = { ":", "/", "@", "=", ">" }
local initial = {} -- recorded by setup(), after the exercise's own setup commands have run

local function normal_windows()
  return vim.tbl_filter(function(w) return api.nvim_win_get_config(w).relative == "" end,
    api.nvim_tabpage_list_wins(0))
end

-- Each window in the layout, in order: what it shows, where its cursor is, and its alternate file.
local function remember_windows()
  initial.windows = {}
  for i, w in ipairs(normal_windows()) do
    initial.windows[i] = api.nvim_win_call(w, function()
      local alt = vim.fn.bufnr("#")
      return { win = w, buf = api.nvim_get_current_buf(), name = api.nvim_buf_get_name(0),
        view = vim.fn.winsaveview(), alt = alt > 0 and api.nvim_buf_get_name(alt) or "" }
    end)
    if w == api.nvim_get_current_win() then initial.current = i end
  end
  initial.sizes = vim.fn.winrestcmd()
end

local function remember_initial_state()
  initial.buffers = {} -- buffer -> its '[ and '] marks (reading the file sets them to its first and last line)
  for _, b in ipairs(api.nvim_list_bufs()) do
    initial.buffers[b] = api.nvim_buf_call(b, function() return { vim.fn.getpos("'["), vim.fn.getpos("']") } end)
  end
  initial.args = vim.fn.argv()
  remember_windows()
  initial.registers = {}
  for _, r in ipairs(REGISTERS) do initial.registers[r] = vim.fn.getreginfo(r) end
  initial.history = {}
  for _, h in ipairs(HISTORIES) do
    local entries = {}
    for i = 1, vim.fn.histnr(h) do
      local e = vim.fn.histget(h, i)
      if e ~= "" then entries[#entries + 1] = e end
    end
    initial.history[h] = entries
  end
end

local typed_command = true -- false after F5 until you run an Ex command yourself (see the @: mapping)
local build_layout -- defined below: the task, target and setup windows
local target_buf -- the scratch buffer the target window shows

function M.restart()
  paused = true
  if vim.fn.reg_recording() ~= "" then vim.cmd("normal! q") end

  -- Make ., & and ; forget the last attempt: throwaway edits in a scratch buffer, and a cleared f/t search.
  local scratch = api.nvim_create_buf(false, true)
  api.nvim_buf_set_lines(scratch, 0, -1, false, { "ab" })
  api.nvim_buf_call(scratch, function()
    vim.cmd("normal! x")
    vim.cmd("silent! s/vimcourse-reset//e")
  end)
  api.nvim_buf_delete(scratch, { force = true })
  vim.fn.setcharsearch({ char = "" })

  pcall(vim.cmd, "cclose | lclose")
  vim.fn.setqflist({}, "f")
  pcall(vim.cmd, "silent %argdelete")
  for _, a in ipairs(initial.args) do pcall(vim.cmd, "silent argadd " .. vim.fn.fnameescape(a)) end

  for _, f in ipairs(S.files) do
    local b = find_buf(f.path)
    if b and api.nvim_buf_is_loaded(b) then
      local levels = vim.bo[b].undolevels
      vim.bo[b].undolevels = -1 -- so undo can't reach back into the previous attempt
      api.nvim_buf_set_lines(b, 0, -1, false, f.start)
      vim.bo[b].undolevels = levels
      -- Saved by Neovim itself: if the file changed behind its back, your next :w or ZZ would stop
      -- to ask "The file has been changed since reading it!!! Do you really want to write to it?"
      api.nvim_buf_call(b, function() vim.cmd("silent noautocmd keepalt write!") end)
    else
      vim.fn.writefile(f.start, f.path)
    end
  end
  -- Windows. If you closed one that was there at the start, rebuild the whole layout. Then close any
  -- you opened, and put each original window back on its file, cursor position and size.
  local intact = true
  for _, e in ipairs(initial.windows) do
    intact = intact and api.nvim_win_is_valid(e.win) and api.nvim_buf_is_valid(e.buf) -- e.g. :bw on the target
  end
  if work_win and api.nvim_win_is_valid(work_win) then
    api.nvim_set_current_win(work_win)
    if not intact then
      pcall(vim.cmd, "silent! only!")
      local open = S.files[S.open]
      if api.nvim_buf_get_name(0) ~= open.path then vim.cmd("silent edit " .. vim.fn.fnameescape(open.path)) end
      build_layout()
      local wins = normal_windows()
      if #wins == #initial.windows then
        for i, e in ipairs(initial.windows) do
          e.win, e.buf = wins[i], api.nvim_win_get_buf(wins[i])
        end
      end
    end
    local keep = {}
    for _, e in ipairs(initial.windows) do keep[e.win] = true end
    for _, w in ipairs(normal_windows()) do
      if not keep[w] then pcall(api.nvim_win_close, w, true) end
    end
    for _, e in ipairs(initial.windows) do
      if api.nvim_win_is_valid(e.win) then
        api.nvim_win_call(e.win, function()
          if api.nvim_buf_is_valid(e.buf) then
            api.nvim_win_set_buf(e.win, e.buf)
          elseif e.name ~= "" then
            pcall(vim.cmd, "silent keepalt edit " .. vim.fn.fnameescape(e.name))
          end
          vim.fn.winrestview(e.view)
          if e.alt ~= "" and vim.fn.bufexists(e.alt) == 1 then
            pcall(vim.cmd, "silent balt " .. vim.fn.fnameescape(e.alt))
          else
            pcall(vim.cmd, "silent balt vimcourse-none | silent bwipeout vimcourse-none")
          end
          pcall(vim.cmd, "clearjumps")
        end)
      end
    end
    pcall(vim.cmd, initial.sizes)
    local current = initial.windows[initial.current]
    api.nvim_set_current_win(current and api.nvim_win_is_valid(current.win) and current.win or work_win)
  end
  for _, b in ipairs(api.nvim_list_bufs()) do
    if not initial.buffers[b] and vim.fn.bufwinid(b) == -1 then pcall(api.nvim_buf_delete, b, { force = true }) end
  end
  for b, op in pairs(initial.buffers) do
    if api.nvim_buf_is_valid(b) then
      pcall(api.nvim_buf_call, b, function()
        vim.cmd("delmarks!")
        vim.fn.setpos("'[", op[1])
        vim.fn.setpos("']", op[2])
      end)
    end
  end
  pcall(vim.cmd, "delmarks A-Z0-9")


  for _, r in ipairs(REGISTERS) do pcall(vim.fn.setreg, r, initial.registers[r]) end
  for _, h in ipairs(HISTORIES) do
    vim.fn.histdel(h)
    for _, e in ipairs(initial.history[h]) do vim.fn.histadd(h, e) end
  end
  pcall(vim.fn.setpos, "'<", { 0, 0, 0, 0 })
  pcall(vim.fn.setpos, "'>", { 0, 0, 0, 0 })
  pcall(vim.cmd, "nohlsearch")
  typed_command = false
  log, final = {}, nil
  last_sig = signature()
  paused = false
  pcall(vim.cmd, "redrawstatus!")
end

-- ---------- F1: notes on the commands this exercise uses ----------
-- A floating window over the top right that doesn't take the cursor, so you can keep typing (in any
-- mode) while it's open. F1 again hides it.

local help_win
function M.help()
  if help_win and api.nvim_win_is_valid(help_win) then
    api.nvim_win_close(help_win, true)
    help_win = nil
    return
  end
  local lines = S.help or {}
  if #lines == 0 then
    api.nvim_echo({ { "No command notes for this one." } }, false, {})
    return
  end
  local buf = api.nvim_create_buf(false, true)
  api.nvim_buf_set_lines(buf, 0, -1, false, lines)
  local ns = api.nvim_create_namespace("vimcourse_help")
  for i, line in ipairs(lines) do
    if line ~= "" and not line:match("^%s") then -- a command's heading
      api.nvim_buf_set_extmark(buf, ns, i - 1, 0, { end_col = #line, hl_group = "Title" })
    end
  end
  vim.bo[buf].modifiable = false
  local width = 20
  for _, line in ipairs(lines) do width = math.max(width, vim.fn.strdisplaywidth(line)) end
  width = math.min(width + 1, vim.o.columns - 4)
  help_win = api.nvim_open_win(buf, false, {
    relative = "editor", anchor = "NE", row = 1, col = vim.o.columns - 1, width = width, height = 1,
    style = "minimal", border = "rounded", focusable = false, zindex = 60,
    title = S.help_title or " the commands for this one ", title_pos = "center", footer = " F1 hides this ", footer_pos = "right",
  })
  vim.wo[help_win].wrap, vim.wo[help_win].linebreak = true, true
  local height = api.nvim_win_text_height(help_win, {}).all
  api.nvim_win_set_height(help_win, math.max(1, math.min(height, vim.o.lines - 6)))
end

-- ---------- layout: task on top, your file on the left, the target on the right ----------

local setup_keys -- defined below: F1, F5, @: and what happens when you quit

local function setup()
  work_win = api.nvim_get_current_win()
  vim.o.laststatus = 3 -- one status line at the bottom instead of one per window
  vim.o.complete = ".,b,u,t" -- Ctrl-n and Ctrl-x Ctrl-l can't copy from the target window (it isn't listed)
  vim.opt.diffopt:append("iwhiteeol") -- grading ignores trailing spaces, so the diff does too
  build_layout()
  last_sig = signature()
  remember_initial_state()
  setup_keys()
end

-- The windows around yours: the task on top, the target on the right, then the exercise's own setup
-- commands. F5 runs this again if you closed one of them.
build_layout = function()
  local open = S.files[S.open]

  if #S.task > 0 then
    vim.cmd("topleft new")
    local win, buf = api.nvim_get_current_win(), api.nvim_get_current_buf()
    vim.bo[buf].buftype = "nofile"
    vim.bo[buf].bufhidden = "wipe"
    vim.bo[buf].buflisted = false -- keep it out of :ls, :bnext and :bufdo"
    api.nvim_buf_set_lines(buf, 0, -1, false, S.task)
    vim.bo[buf].modifiable = false
    local wo = vim.wo[win]
    wo.number, wo.relativenumber, wo.cursorline = false, false, false
    wo.wrap, wo.linebreak, wo.winfixheight = true, true, true
    -- %< : on a narrow screen, cut the key hints rather than the title
    wo.winbar = string.format(" %%#Title#%s · %s%%*%%=%%<%%#Comment#%s%%* ", esc(S.label), esc(S.title),
      S.mode == "watch" and "watching the reference solution" or "F1 help · F5 restart · F7/F9 back/next · ZZ submit")
    api.nvim_win_set_height(win, math.min(api.nvim_win_text_height(win, {}).all + 1, 11)) -- +1: the winbar
    api.nvim_set_current_win(work_win)
  end

  if open.target then
    -- A scratch buffer, not a file: there's nothing on disk to :read or :e the answer from.
    vim.cmd("rightbelow vsplit")
    local target_win = api.nvim_get_current_win()
    if not (target_buf and api.nvim_buf_is_valid(target_buf)) then
      target_buf = api.nvim_create_buf(false, true) -- unlisted, nofile, no swap file
      api.nvim_buf_set_lines(target_buf, 0, -1, false, open.target)
      pcall(api.nvim_buf_set_name, target_buf, "target: " .. vim.fn.fnamemodify(open.path, ":t"))
      vim.bo[target_buf].filetype = vim.filetype.match({ filename = open.path, buf = target_buf }) or ""
      vim.bo[target_buf].readonly, vim.bo[target_buf].modifiable = true, false
    end
    api.nvim_win_set_buf(target_win, target_buf)
    vim.wo[target_win].winbar = " %#Comment#target: make your file match this%*"
    vim.cmd("diffthis")
    api.nvim_set_current_win(work_win)
    vim.cmd("diffthis")
    for _, w in ipairs({ work_win, target_win }) do
      vim.wo[w].foldenable = false
      vim.wo[w].foldcolumn = "0"
    end
  end

  for _, cmd in ipairs(S.setup) do vim.cmd(cmd) end
  vim.wo[work_win].winbar = "%!v:lua.VimCourse.winbar()"
  api.nvim_win_set_cursor(work_win, { S.cursor[1], S.cursor[2] - 1 })
end

setup_keys = function()
  vim.keymap.set("n", "<F5>", "<Cmd>lua VimCourse.restart()<CR>", { desc = "Restart the exercise" })
  -- @: repeats the last command line, which Neovim only lets typed keys reset. So after F5, @: does
  -- nothing until you've typed an Ex command in this attempt.
  api.nvim_create_autocmd({ "CmdlineEnter", "CmdwinEnter" }, {
    pattern = ":",
    callback = function() if not paused then typed_command = true end end,
  })
  vim.keymap.set({ "n", "x" }, "@:", function()
    if typed_command then return "@:" end
    return "<Cmd>echohl ErrorMsg | echo 'E30: No previous command line' | echohl None<CR>"
  end, { expr = true, desc = "@:, except the previous attempt's command" })
  vim.keymap.set({ "i", "x", "s", "o" }, "<F5>", "<Esc><Cmd>lua VimCourse.restart()<CR>",
    { desc = "Restart the exercise" })
  vim.keymap.set({ "n", "i", "x", "s", "c" }, "<F1>", "<Cmd>lua VimCourse.help()<CR>",
    { desc = "Show or hide notes on this exercise's commands" })
  if S.mode == "play" then
    for key, where in pairs({ ["<F7>"] = "prev", ["<F8>"] = "menu", ["<F9>"] = "next" }) do
      vim.keymap.set({ "n", "i", "x", "s", "o", "c" }, key, "<Cmd>lua VimCourse.leave('" .. where .. "')<CR>",
        { desc = "Leave without grading: to the " .. (where == "menu" and "menu" or where .. " exercise") })
    end
  end

  -- Quitting your file's window (ZZ, :wq, :q!, ...) ends the exercise. The text is snapshotted just
  -- before any quit, and frozen once your window closes (after :q! the buffer is already discarded).
  local closing = false
  api.nvim_create_autocmd("WinClosed", {
    pattern = tostring(work_win),
    callback = function()
      if not final then pcall(snapshot) end -- e.g. Ctrl-w c, which skips QuitPre
      closing = true
      vim.schedule(function() vim.cmd("qa!") end)
    end,
  })
  api.nvim_create_autocmd({ "QuitPre", "ExitPre" }, {
    callback = function() if not closing then pcall(snapshot) end end,
  })
  api.nvim_create_autocmd("VimLeavePre", { callback = function() if S.mode ~= "watch" then write_result() end end })
end

-- F7, F8 and F9: quit without grading, and tell check.py to go to the previous exercise, back to its
-- menu, or to the next one.
function M.leave(where)
  leaving = where
  vim.cmd("qa!")
end

-- ---------- replay: check.py types the reference solution through Neovim's RPC socket ----------

-- Called by check.py (as <Cmd>lua VimCourse.finish()<CR>) after the last key of a replay.
function M.finish()
  done = true
  if S.mode == "watch" then
    pcall(vim.cmd, "redrawstatus!")
    return
  end
  snapshot()
  if coach then
    local fin = coach.state(signature(), function() return file_lines(S.files[1]) end)
    local ok, found = pcall(coach.analyze, log, fin, S.analyze.level, S.analyze.budget, work_win)
    coached = ok and found or { error = tostring(found) }
    -- The coach tried its ideas in your buffer: put your text back, since quitting snapshots it again.
    local b = find_buf(S.files[1].path)
    if b then pcall(api.nvim_buf_set_lines, b, 0, -1, false, final.files[1]) end
  end
  write_result()
  vim.cmd("qa!")
end

setup()
