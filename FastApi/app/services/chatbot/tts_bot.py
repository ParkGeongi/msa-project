from gtts import gTTS
from playsound import playsound
import random

from app.admin.path import dir_path


class Tts:

    def __init__(self):
        self.text = ''

    @staticmethod
    def run(input_text):
        tts = gTTS(text=input_text, lang="ko")
        #title = random.randrange(1, 999999999999999)
        title = '2'
        path = dir_path(param="chatbot") + '/save_mp3'
        #tts.save(f"{path}/{title}.mp3")
        tts.save('./1.mp3')
        #playsound(f"{path}/{title}.mp3")
        playsound(f"./1.mp3")


'''
Tts().run(answer)
        sleep(3)
        path = dir_path(param="chatbot") + '/save_mp3'
        playsound(f"{path}/1.mp3")
'''

if __name__ == '__main__':
    Tts().run('안녕하세요반가워요')
    