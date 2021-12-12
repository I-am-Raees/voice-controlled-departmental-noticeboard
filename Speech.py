import speech_recognition as sr
import pyttsx3
from SysPaths import *
from Authentication.OpenFile import *

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def say(text):
    """[It narrates up the text and wait until all the text is spoken out.]

    Args:
        text ([string]): [the text to be narrated.]
    """
    engine.say(text)
    engine.runAndWait()

def speak():
    """[It recognizes the speech and converts into the text.
    It takes in the pyttsx3 engine to speak out the errors if encountered.]

    Args:
        engine ([pyttsx3.Engine]): [For the system to speak out the information or alerts]

    Returns:
        [string]: [The text of speech understood by the google API]
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)            
        except sr.UnknownValueError:
            engine.say("Google Speech Recognition could not understand audio")
            return ""
        except sr.RequestError as e:
            engine.say("Could not request results from Google Speech Recognition service; {0}".format(e))
            return ""
        except Exception as e:
            engine.say("Oooops, an error occurred: ")
            engine.say(str(e))
            print(e)
            return ""
        finally:
            engine.runAndWait()
