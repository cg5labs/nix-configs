#!/usr/bin/env python3

"""
Management script for dotfiles.
Links dotfiles from CVS to their system locations.
Called from wrapper-script manage_dotfiles.sh.
"""

from pathlib import Path

import os
import sys
import logging
import yaml

##############################
# set defaults and load config
##############################

default_path = os.environ['HOME']
source_path = ("%s/%s" % (default_path, "nix-configs"))

# TODO: Set log-level in environment, use default if unset
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, \
                    datefmt='%Y-%m-%d %H:%M:%S')

# load configfile
# TODO: check if config file exists
with open("dotfiles.yml", 'r') as dotfile_config:
    dotfiles = yaml.safe_load(dotfile_config)

###########
# functions
###########

def set_target_path(conf):
    if conf['file_path'] == "default":
        logging.debug("target: %s/%s", default_path, conf['file_src'])
        target_path = default_path
    else:
        target_path = ("%s/%s" % (default_path, conf['file_path']))
        logging.debug("target: %s/%s", target_path, conf['file_tgt'])
    return target_path

def verify_target_path(target_path):
    verify_status = bool(os.path.isdir(target_path))
    return verify_status

def verify_target_file(target_file):
    verify_status = bool(os.path.isfile(target_file))
    return verify_status

def verify_source_file(source_file):
    verify_status = bool(os.path.isfile("%s/%s" % (source_path, source_file)))
    return verify_status

######
# main
######

# change into $HOME and rewrite cfg_path_abs as relative
os.chdir(default_path)

logging.debug(yaml.dump(dotfiles))

for config in dotfiles:

    CHECK_SOURCE_FILE = verify_source_file(config['file_src'])

    if not CHECK_SOURCE_FILE:
        logging.error("Error! Source file missing: %s/%s", source_path, \
            config['file_src'])

    if 'file_platform' in config:
        logging.debug("checking for OS: %s", config['file_platform'])

        if config['file_platform'] != sys.platform:
            logging.debug("file_platform not detected, skipping: %s for %s", \
                config['file_platform'], config['file_src'])
            continue

    link_target_path = set_target_path(config)
    logging.debug("link target path set: %s", link_target_path)

    CHECK_TARGET_PATH = verify_target_path(link_target_path)

    if not CHECK_TARGET_PATH:
        logging.info("creating target path: %s", link_target_path)

        # TODO: try-catch exceptions
        Path(link_target_path).mkdir(parents=True, exist_ok=True)

    if 'file_tgt' in config:
        CHECK_FILE = verify_target_file("%s/%s" % (link_target_path, \
            config['file_tgt']))

        if CHECK_FILE:
            logging.info("target file exists: %s/%s", link_target_path, \
                config['file_tgt'])
        else:
            logging.info("creating symlink: %s/%s -> %s/%s", source_path, \
                config['file_src'], link_target_path, config['file_tgt'])

            cfg_path = os.path.relpath(source_path, link_target_path)
            link_tgt_file = ("%s/%s" % (link_target_path, config['file_tgt']))
            link_src_file_rel = ("%s/%s" % (cfg_path, config['file_src']))
            logging.debug("link src: %s", link_src_file_rel)
            logging.debug("link tgt: %s", link_tgt_file)

            # TODO: try-catch exceptions
            os.symlink(link_src_file_rel, link_tgt_file)

    else:
        CHECK_FILE = verify_target_file("%s/%s" % (link_target_path, \
            config['file_src']))

        if CHECK_FILE:
            logging.info("target file exists: %s/%s", link_target_path, \
                config['file_src'])

        else:
            logging.info("creating symlink: %s/%s -> %s/%s", source_path, \
                config['file_src'], link_target_path, config['file_src'])

            cfg_path = os.path.relpath(source_path, link_target_path)
            link_tgt_file = ("%s/%s" % (link_target_path, config['file_src']))
            link_src_file_rel = ("%s/%s" % (cfg_path, config['file_src']))
            logging.debug("link src: %s", link_src_file_rel)
            logging.debug("link tgt: %s", link_tgt_file)

            # TODO: try-catch exceptions
            os.symlink(link_src_file_rel, link_tgt_file)
