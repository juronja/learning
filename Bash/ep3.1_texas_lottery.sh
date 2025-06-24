#! /bin/bash

rnr1=$((RANDOM%55))
rnr2=$((RANDOM%55))
rnr3=$((RANDOM%55))
rnr4=$((RANDOM%55))
rnr5=$((RANDOM%55))
rnr6=$((RANDOM%55))


echo "Hello doode, write down 6 random numbers between 0-54 for the lottery please. Seperated by comma."
read wnr
sleep 2
echo "The winning numbers are:"
echo $rnr1,$rnr2,$rnr3,$rnr4,$rnr5,$rnr6
echo "Your numbers were:"
echo $wnr
