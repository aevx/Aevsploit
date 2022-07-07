red='\033[0;31m'
yesil='\033[0;32m'
dur='\033[0m'

printf "${red}Konum: ${yesil}"
curl -s "https://api.evozi.com/ip_ui" | tr -d "" | grep -Po '(?<=<p><small>).*?(?=<)' | sed '$d'
printf "${dur}"
printf "${red}Dinamik ip: ${yesil}"
curl -s "https://api.evozi.com/ip_ui" | tr -d "" | grep -Po '(?<=<div class="title">).*?(?=<)'
printf "${dur}"
