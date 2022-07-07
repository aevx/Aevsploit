xterm -geometry 90x26+1000 -T "PHP server" -hold -e "php -S 127.0.0.1:3333" > /dev/null 2>&1 &
xterm -T "NGROK server" -geometry 90x26+1000+1000 -hold -e "/usr/local/bin/ngrok http 3333" > /dev/null 2>&1 &

link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")
printf "${BYellow}Your Domain is:${BGreen} %s\e[0m\n" $link
