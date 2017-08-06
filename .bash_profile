# OS probe
unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     OS=Linux;;
    Darwin*)    OS=Mac;;
    CYGWIN*)    OS=Cygwin;;
    MINGW*)     OS=MinGw;;
    *)          OS="UNKNOWN:${unameOut}"
esac


# user-specific aliases

if [[ ${OS} == "Mac" ]]; then
  export LSCOLORS="gxBxhxDxfxhxhxhxhxcxcx"
  alias ll='ls -l -G'
fi

if [[ ${OS} == "Linux" ]]; then
  # change dir color for ls
  LS_COLORS=$LS_COLORS:'di=1;32:' ; export LS_COLORS
  alias ll='ls -l --color=auto'
fi

