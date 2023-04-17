import speech_recognition as sr
import threading
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from playsound import playsound

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def intro():
    engine.say('hi i am barbie.... your personal assistant')
    engine.say('how can i help you')
    engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def mic_thread(y, z):
    try:
        delay = int(y)
        start_time = threading.Timer(delay, z)
        start_time.start()
    except:
        pass


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


def call(x):
    def take_command():
        print("say command..")
        # mic_thread(4, take_command)
        command_taken = microphone()
        return command_taken

    if x == 1:
        command = take_command()

    else:
        print('call barbie')
        # mic_thread(4, call)
        command = microphone()
        if 'barbie' in command:
            playsound('listning_sound.wav')
            print('detected command ' + command)
            talk('yes....i am listening...')
            call(1)
        else:
            call(0)
    return command


def run_assistant():
    while True:
        run_command = call(0)
        playsound('got_it_sound.wav')
        print(run_command)
        while True:
            if 'play' in run_command:
                print('playing...')
                song = run_command.replace('play', '')
                talk('playing' + song)
                pywhatkit.playonyt(song)
                break
            elif 'what is' in run_command:
                print('question 1')
                talk('let me check the web for you')
                question = run_command.replace('what is', '')
                info = wikipedia.summary(question, 2)
                print(info)
                talk(info)
                break
            elif 'who is ' in run_command:
                print('question 2')
                talk('let me check the web for you')
                question = run_command.replace('who is', '')
                info = wikipedia.summary(question, 1)
                print(info)
                talk(info)
                break
            elif 'joke' in run_command:
                print('question 3')
                talk('get ready to laugh your ass off')
                joke = pyjokes.get_joke()
                talk(joke)
                talk('ha...ha...ha...ha.')
                print(joke)
                break
            elif 'introduce your self' in run_command:
                print("introducing")
                intro()
                break
            elif 'time' in run_command:
                print('displaying time')
                talk('your time is not correct for sure')
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                talk('current time is.' + time)
                break
            elif 'thankyou' in run_command:
                print("welcome note")
                talk('you are welcome master')
                talk('you are my hero master ')
                break

            else:
                print('sorry can you repeat')
                talk('sorry can you repeat')
                run_command = call(1)

    run_assistant()


# intro()
run_assistant()
