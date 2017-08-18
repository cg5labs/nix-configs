# OS probe
# TODO: refactor to external script
unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     OS=Linux;;
    Darwin*)    OS=Mac;;
    CYGWIN*)    OS=Cygwin;;
    MINGW*)     OS=MinGw;;
    *)          OS="UNKNOWN:${unameOut}"
esac


# general config

# git-aware prompt
# https://github.com/jimeh/git-aware-prompt

if [[ -d ${HOME}/.bash ]]; then
  export GITAWAREPROMPT=~/.bash/git-aware-prompt
  source "${GITAWAREPROMPT}/main.sh"
fi

# OS-specific configs
if [[ ${OS} == "Mac" ]]; then
  if [[ -f ${HOME}/nix-configs/.bash_profile_osx ]]; then
    source ${HOME}/nix-configs/.bash_profile_osx
  else
    echo "==> error loading ${HOME}/nix-configs/.bash_profile_osx"
  fi
fi

if [[ ${OS} == "Linux" ]]; then

  # Linux shared configs

  # change dir color for ls
  LS_COLORS=$LS_COLORS:'di=1;32:' ; export LS_COLORS
  alias ll='ls -la --color=auto'

  # OpenSUSE configs
  if [[ -r /etc/SuSE-release || $(grep suse /etc/os-release) == 0 ]]; then
    if [[ -f ${HOME}/nix-configs/.bash_profile_suse ]]; then
      source ${HOME}/nix-configs/.bash_profile_suse
    else
      echo "==> error loading ${HOME}/nix-configs/.bash_profile_suse"
    fi
  fi

fi

