#!/usr/bin/expect

expect -c "

spawn ssh root@47.89.209.49

expect {

\"*assword\" {set timeout 30; send \"xxx\r\";}

\"yes/no\" {send \"yes\r\"; exp_continue;}

}

send \"cd servergit \r\"
send \"cd idol \r\"
send \"git pull \r\"

expect eof"
