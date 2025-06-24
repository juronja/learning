#! /bin/bash


echo "Hello hooman, what is your name?"
read name
echo "And you how old are you?"
read age
sleep 1
echo "Hello, $name, you are $age years old."

#echo "$PWD, $SHELL, $USER, $HOSTNAME" sistem backed in variables

getrich=$(((RANDOM%15)+$age))

echo "Hey, you are going to become a millionaire at $getrich"

