#!/usr/bin/env bash

######################################################################
# @author      : Óscar Heredia (65867332+OscHer@users.noreply.github.com)
# @file        : bootstrap.sh
# @created     : sábado ene 18, 2025 12:21:21 CET
#
# @description : Bootstrap script for setting up a python development laboratory
######################################################################

apt-get update && apt-get upgrade -y
apt-get install -y git vim tmux bash-completion universal-ctags
