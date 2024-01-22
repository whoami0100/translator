#!/bin/bash

echo "--------- A speech translator tool based on python ---------"
echo "1.traslator any word in any language"
echo "2.text to speech converter"
echo "enter any keyword from above list 1-2:"
read option
if [ $option == 1 ]
then
python3 py/main.py
sudo systemctl start apache2.service 
cp *mp3 /var/www/html
mv *mp3 audio
elif [ $option == 2 ]
then
python3 py/speech.py
cp *mp3 /var/www/html
mv *mp3 audio
fi 

echo "are you want to play that audio [yes|no]:"
read option1
if [ $option1 == yes ]
then 
echo "enter the name of file that are name before:"
read option3
open audio/$option3
elif [ $option1 == no ]
then
echo "ok....."
else 
echo "invalid option"
fi 
