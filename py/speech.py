# Import the required module for text 
# to speech conversion 

from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 

# The text that you want to convert to audio 

mytext =input("enter any keyword to convert to speech:")

# Language in which you want to convert 
language =input("enter the language in which to play the audio file:")

# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named  
file_name=input("enter the name of the file to save with .mp3 formate [e.g. test.mp3]:")
myobj.save(file_name)  

