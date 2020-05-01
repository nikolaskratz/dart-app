import speech_recognition as sr
import os


def get_audio_input():
    r = sr.Recognizer()
    int_detected = False
    listen = True
    text = ""
    with sr.Microphone() as source:
        while listen:
            audio = r.listen(source, phrase_time_limit=2)
            try:
                text = r.recognize_google(audio)
                if "correction" in text:
                    listen = False
                    speak("Correction")
                    return get_audio_input()[0], True
                else:
                    try:
                        int(text)
                        int_detected = True
                    except:
                        pass
                    if int_detected:
                        speak(text)
                        listen = False
                        return int(text), False
            except:
                pass

def speak(input):
    os.system("espeak '{}'".format(input))


