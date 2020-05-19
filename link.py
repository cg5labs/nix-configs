#!/usr/bin/env python

"""
!!! OBSOLETE -- USE manage_dotfiles.sh INSTEAD !!!

This script links dotfiles from CVS to their system locations
"""

import os

# config section  - start

# add dotfiles in array to be created at default location ($HOME/.dotfile)
cfg_files_default = [
    '.vimrc',        # vim
    '.tmux.conf',    # tmux
    '.bash_profile', # bash
    '.xmodmap'       # xmodmap
    '.testcfg'       # dummy link
    ]

# add dotfiles in dictionary to be created at target location ($HOME/<target_path>/.dotfile)
cfg_files_custom = [
    {
        'file_location': ".config/yamllint",  # yamllint
        'file_name': "config"
    }
]

# config section - end

#
# main
#

#
# dotfiles in default location ($HOME/.dotfile)
#

home_path_abs = os.environ['HOME']
cfg_path_abs = (("%s/%s") % (home_path_abs, "nix-configs"))

# change into $HOME and rewrite cfg_path_abs as relative
os.chdir(home_path_abs)

cfg_path = os.path.relpath(cfg_path_abs, home_path_abs)

for list_file in cfg_files_default:

    # source for symlink
    link_dotfile = ("%s/%s" % (cfg_path, list_file))

    # check if symlink source exists
    link_dotfile_status = os.path.isfile(link_dotfile)
    if not link_dotfile_status:
        print("==> symlink source missing: %s" % (link_dotfile))
        break

    # target location for symlink
    home_dotfile = ("%s/%s" % (home_path_abs, list_file))

    # skip if dotfile exists either as link or as file
    if os.path.isfile(home_dotfile):
        print("==> dotfile exists, skipping symlink: %s" % (home_dotfile))

    if not os.path.islink(home_dotfile):
        print("==> symlink missing: %s" % (home_dotfile))
        os.symlink(link_dotfile, home_dotfile)
        print("==> symlink created: %s" % (home_dotfile))

#
# dotfiles in custom locations ($HOME/<location>/.dotfile)
#

home_path_abs = os.environ['HOME']
cfg_path_abs = (("%s/%s") % (home_path_abs, "nix-configs"))

# change into $HOME and rewrite cfg_path_abs as relative
os.chdir(home_path_abs)

for cfg_file in cfg_files_custom:
    cfg_path_abs = ("%s/%s" % (home_path_abs, cfg_file['file_location']))
    cfg_path = os.path.relpath(cfg_path_abs, home_path_abs)
    custom_dotfile_abs = ("%s/%s" % (cfg_path_abs, cfg_file['file_name']))
    custom_dotfile = ("%s/%s" % (cfg_path, cfg_file['file_name']))

    if os.path.isfile(custom_dotfile_abs):
        print("==> dotfile exists, skipping symlink: %s" % (custom_dotfile_abs))

    if not os.path.isfile(custom_dotfile_abs):
        print("==> dotfile does not exist, creating symlink: %s" % (custom_dotfile_abs))

