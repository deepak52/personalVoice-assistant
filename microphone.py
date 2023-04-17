import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

r = sr.Recognizer()
    with sr.Microphone() as source:
        print("microphone activated!")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition
    try:
        var = r.recognize_google(audio)
    except sr.UnknownValueError:
        var = "Groot could not understand audio"
    except sr.RequestError:
        var = " Looks like, there is some problem with Google Speech Recognition"
    var = var.lower()
    print(var)
    print('microphone deactivated')

print( var)


