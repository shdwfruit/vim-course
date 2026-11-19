-- Editor settings for course exercises. You never need to edit this.
--
-- Every exercise runs with exactly this setup instead of your ~/.config/nvim, so the results and
-- the par (target key count) are the same every time, even after you change your own config.
-- It mirrors your config: same indentation, search, and line-number settings.

vim.cmd.colorscheme("catppuccin")
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.cursorline = true

vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true
vim.opt.smartindent = true

vim.opt.ignorecase = true
vim.opt.smartcase = true

-- Keep each attempt independent: no swap files, no undo history or registers from earlier attempts.
vim.opt.swapfile = false
vim.opt.undofile = false
vim.opt.shortmess:append("I")
