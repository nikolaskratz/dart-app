import speech_recognition as sr
import os


def listen_for_int():
    r = sr.Recognizer()
    listen = True
    int_detected = False
    text = ""
    with sr.Microphone() as source:
        while listen:
            audio = r.listen(source, phrase_time_limit=3)
            try:
                text = r.recognize_google(audio)
                try:
                    int(text)
                    int_detected = True
                except:
                    pass
                if int_detected:
                    # print(text)
                    speak(text)
                    listen = False
                    return int(text)
            except:
                pass

def speak(input):
    os.system("espeak '{}'".format(input))
