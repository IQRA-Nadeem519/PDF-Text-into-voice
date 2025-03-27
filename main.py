from PyPDF2 import PdfReader
from gtts import gTTS
import os

reader = PdfReader("crimestory.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text()
# print(text)
tts = gTTS(text=text, lang='en')  
tts.save("output.mp3")
os.system("start output.mp3")
