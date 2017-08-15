#!/usr/bin/python

import os

# config section

# add dotfiles in array to be created
cfg_files  = [
  '.vimrc',        # vim
  '.tmux.conf',    # tmux
  '.bash_profile', # bash
  '.testcfg'       # dummy link
  ]

# main

home_path_abs = os.environ['HOME']
cfg_path_abs  = (("%s/%s") % (home_path_abs,"nix-configs"))

# change into $HOME and rewrite cfg_path_abs as relative
os.chdir(home_path_abs)

cfg_path = os.path.relpath(cfg_path_abs, home_path_abs)

for list_file in cfg_files:

    # source for symlink
    link_dotfile = ("%s/%s" % (cfg_path,list_file))

    # check if symlink source exists
    link_dotfile_status = os.path.isfile(link_dotfile)
    if link_dotfile_status == False:
        print("==> symlink source missing: %s" % (link_dotfile))
        break

    # target location for symlink
    home_dotfile = ("%s/%s" % (home_path_abs,list_file))

    # skip if dotfile exists either as link or as file
    if os.path.isfile(home_dotfile):
        print("==> dotfile exists, skipping symlink: %s" % (home_dotfile))

    if not os.path.islink(home_dotfile):
        print("==> symlink missing: %s" % (home_dotfile))
        os.symlink(link_dotfile, home_dotfile)
        print("==> symlink created: %s" % (home_dotfile))

