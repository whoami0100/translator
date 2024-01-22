from deep_translator import GoogleTranslator
from gtts import gTTS 
import os

lan=input("enter language in which you want to translate:")
t=GoogleTranslator(
 source="auto",
 target=lan
)
keyword=input("enter any keyword you want to translate:")
print("you keyword or phases in translating just wait for few soconds......") 
mytext=t.translate(keyword)

print(mytext)

language =lan
   
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named  
filename=input("enter the name of file to stored save with .mp3 formate [e.g test.mp3]:")
myobj.save(filename) 
print("you audio file has been stored in audio/"+filename)
   

