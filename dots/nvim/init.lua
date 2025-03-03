require("gyaf")
-- Bootstrap lazy.nvim
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not (vim.uv or vim.loop).fs_stat(lazypath) then
  local lazyrepo = "https://github.com/folke/lazy.nvim.git"
  local out = vim.fn.system({ "git", "clone", "--filter=blob:none", "--branch=stable", lazyrepo, lazypath })
  if vim.v.shell_error ~= 0 then
    vim.api.nvim_echo({
      { "Failed to clone lazy.nvim:\n", "ErrorMsg" },
      { out, "WarningMsg" },
      { "\nPress any key to exit..." },
    }, true, {})
    vim.fn.getchar()
    os.exit(1)
  end
end
vim.opt.rtp:prepend(lazypath)

-- Make sure to setup `mapleader` and `maplocalleader` before
-- loading lazy.nvim so that mappings are correct.
-- This is also a good place to setup other settings (vim.opt)
vim.g.mapleader = " "
vim.g.maplocalleader = "\\"
  
-- Setup lazy.nvim
require("lazy").setup({
  spec = {
      {
          'nvim-telescope/telescope.nvim',
          version = '0.1.8', -- ou use `branch = '0.1.x'`
          dependencies = { 'nvim-lua/plenary.nvim' },
      },
      {
      "dgox16/oldworld.nvim",
      lazy = false,
      priority = 1000,
      },
      'nvim-treesitter/nvim-treesitter',
      'theprimeagen/harpoon',
      'mbbill/undotree',
      'neovim/nvim-lspconfig',
      'hrsh7th/cmp-nvim-lsp',
      'hrsh7th/nvim-cmp',
      'vonheikemen/lsp-zero.nvim',
      'm4xshen/autoclose.nvim',
      {
          'MeanderingProgrammer/render-markdown.nvim',
          dependencies = { 'nvim-treesitter/nvim-treesitter', 'echasnovski/mini.nvim' }, -- if you use the mini.nvim suite
          ---@module 'render-markdown'
          ---@type render.md.UserConfig
          opts = {},
      },
      {'akinsho/toggleterm.nvim', version = "*", config = true},


  },
  -- Configure any other settings here. See the documentation for more details.
  -- colorscheme that will be used when installing plugins.
  -- automatically check for plugin updates
  checker = { enabled = false },
})

