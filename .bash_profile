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
  if [[ -f .bash_profile_osx ]]; then
    source .bash_profile_osx
  else
    echo "==> error loading .bash_profile_osx"
  fi
fi

if [[ ${OS} == "Linux" ]]; then
  # change dir color for ls
  LS_COLORS=$LS_COLORS:'di=1;32:' ; export LS_COLORS
  alias ll='ls -l --color=auto'
fi

