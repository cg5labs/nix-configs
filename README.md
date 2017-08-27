# nix-configs
Default configuration files for Unix systems.

* Dotfiles from nix-configs  will only be symlinked if no corresponding dotfile already exists in $HOME
* Tool-specific dotfiles will only be symlinked if the tool is installed on the system

```python
.tmux.conf     #
.xmodmap       #  custom keyboard (swap ESC + tilde)
.vimrc         #  adapted .vimrc from http://vim.wikia.com/wiki/Example_vimrc
.bash_profile  #  master .bash_profile 
               #  sources OS-specific profiles for:
               #  * Mac OSX
               #  * Linux (Suse)

link.py        #  Automatic check-script to create symlinks if missing: 
               #  $HOME/.dotfile -> $HOME/nix-configs/.dotfile

```

Adding new Dotfiles:
# add file: ./nix-configs/<new-dotfile>
# edit ./nix-configs/link.py (add dotfile to dotfiles array at beginning)
# run ./nix-configs/link.py
