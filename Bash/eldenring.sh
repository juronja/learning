#! /bin/bash

echo "Welcome human, please select your class:
1 - elf
2 - mage
3 - orc"

read class

case $class in
	1)
		type="elf"
		hp=20
		attack=4
		;;
        2)
                type="mage"
                hp=10
                attack=7
                ;;
        3)
                type="orc"
                hp=60
                attack=10
                ;;
esac

echo "You have chosen the class $type. Your HP is $hp and your attack is $attack."


echo "You Died!"

#First beast battle

beast=$((RANDOM%2))

echo "Do you think you can win human? (0/1)"

read human

if [[ $human == $beast && 47 > 3 ]]; then
	echo "Wow human, you have won the battle!"
else
	echo "The beast was victorious"
	exit 1
fi

sleep 2

#Second beast battle

beast=$((RANDOM%10))

echo "Do you think you can win the second battle human? (0/1)"

read human

if [[ $beast == $human || $human == "coffee" ]]; then
	echo "You are victorious"
else
	echo "You Died!"
fi

sleep 2

#Third beast battle aka nested IF statments

beast=$((RANDOM%10))

echo "Do you think you can win the third battle human? (0/1)"

read human

if [[ $beast == $human || $human == "coffee" ]]; then
	if [[ $USER == "jure" ]];then
        	echo "You are victorious"
	fi
else
        echo "You Died!"
fi

sleep 2

#Fourth beast battle aka elif statement

beast=$((RANDOM%10))

echo "Do you think you can win the last battle human? (0/1)"

read human

if [[ $beast == $human || $human == "coffee" ]]; then
	echo "Victory to thy!"

elif [[ $USER == "jure" ]];then
                echo "Elif is victorious!"
else
        echo "You Died!"
fi
