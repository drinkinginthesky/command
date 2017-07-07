#!/usr/bin/expect

expect -c "

spawn ssh ss@192.168.2.29

expect {

\"*assword\" {set timeout 30; send \"ss\r\";}

\"yes/no\" {send \"yes\r\"; exp_continue;}

}

send \"cd servergit \r\"
send \"cd idol \r\"
send \"git pull \r\"
send \"set timeout 50; pm2 restart 0 \r\"

expect eof"
