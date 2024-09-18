import os
import wikipedia
from gtts import gTTS
wikipedia.set_lang('en')
result=wikipedia.summary('Saudi Arabia',sentences=4)
print(result)
myobj=gTTS(text=result,lang="en",slow=False)
myobj.save('saudi.mp3')
os.system('start saudi.mp3')