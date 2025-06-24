#!/bin/bash

name=$1 #this is a possitional parameter
beard=$2
city=$3

user=$(whoami) #pulling data from the linux commands
date=$(date)
whereami=$(pwd)
privateip=$(hostname -I | awk '{print $1}')
publicip=$(curl -s https://ipecho.net/plain)
weather=$(curl -s https://wttr.in/$city?0pq)
dadjoke=$(curl -s -H "Accept:text/plain" https://icanhazdadjoke.com)

#echo "What is your name?"
#read name

echo "good morning $name!"
sleep 1
echo "you are looking good today $name!"
sleep 1
echo "you have the best $beard i've ever seen $name!"
sleep 2
echo "Your are logged in as $user and you are in the directory $whereami. Also  today is $date."

sleep 2

echo "My private ip is $privateip and my public ip is $publicip"

sleep 2

echo "Weather in $city is currently $weather"

sleep 2

echo "Here is a joke of the day: $dadjoke"

