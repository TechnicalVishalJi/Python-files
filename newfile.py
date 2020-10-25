from gtts import gTTS
from playsound import playsound

d = "I am Vishal Singh"
l = 'en'
j = gTTS(text = d, lang = l, slow = False)
j.save("a.mp3")
playsound("a.mp3-")