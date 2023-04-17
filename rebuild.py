import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def microphone():
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
    return var


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'bomma' in command:
                command = command.replace('bomma', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

while True:
    run_alexa()
