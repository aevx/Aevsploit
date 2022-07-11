if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi

PS1='\n\e[1;91m\]┌─\e[1;91m[\[\e[1;97m\]\T\e[1;91m]─────[\e[1;93m\H\e[1;91m]─────[\e[1;91m\e[1;97m\#\e[1;91m]\n│\n├─\e[1;91m[\e[0;37m\w\e[1;91m]\e[1;91m\n│\n\e[1;91m└─[\[\e[1;91m\]\e[1;95mnick\[\e[0m\e[1;91m\]]───┐\n          │\n          \e[1;91m└⊰ \e[0m'

figlet -f Epic "banner" | lolcat

alias aev="cd && cd Aevsploit && python aevsploit.py"
alias Aev="cd && cd Aevsploit && python aevsploit.py"
alias AEV="cd && cd Aevsploi && python aevsploit.py"

alias l="ls -a"
alias ls="ls -a"
alias dir="ls -a"
alias xd="cd"
alias CD="cd"
alias sil="rm -rf"
alias geri="cd ../"
alias usr="cd && cd $PREFIX"
alias etc="cd && cd $PREFIX/etc"
alias e="exit"
alias c="clear"
alias q="exit"
alias gc="git clone"
alias nano="nano -m"
alias p="pwd"
alias py="python"
alias aevsp="cd /sdcard/Aevsploit && python aevsploit.py"
alias aevsp="cd Aevsploit && python aevsploit.py"