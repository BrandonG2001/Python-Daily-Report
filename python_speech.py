#import pyttsx3
from pyttsx3 import init as pyttsx3_init
#from daily_report import MAIN_COMPUTER

ai_voice = pyttsx3_init()
voices = ai_voice.getProperty('voices')


# registry edit to get more voices
try:
    voices_dict = {
                'David' : voices[0].id,
                'Susan' : voices[1].id,
                'Eva' : voices[2].id,
                'Mark' : voices[3].id,
                'Hazel' : voices[4].id,
                'George' : voices[5].id
                }
except:
    voices_dict = {
                'David' : voices[0].id,
                'Susan' : voices[1].id,
                'Eva' : voices[1].id,
                'Mark' : voices[0].id,
                'Hazel' : voices[1].id,
                'George' : voices[0].id
                }
ai_voice.setProperty('rate', 140)
ai_voice.setProperty('voice', voices_dict['Mark'])

def speak(phrase, speed=140):
    ai_voice.setProperty('rate', speed)
    ai_voice.say(phrase)
    ai_voice.runAndWait()
    # this i think solves the disconnecting issues
    #sleep(0.2)

def print_and_speak(phrase, speed=140):
    print(phrase)
    speak(f'{phrase.strip()},', speed=speed)

def set_ai_voice(name):
    ai_voice.setProperty('voice', voices_dict[name])

def test_voices():
    for voice in voices_dict:
        print(voice, voices_dict[voice])
        ai_voice.setProperty('voice', voices_dict[voice])
        ai_voice.say("Hello World!")
        ai_voice.runAndWait()
        ai_voice.stop()
