import speech_recognition as sr
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
    engine.say('hi i am alexa.... your personal assistant')
    engine.say('how can i help you')
    engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def call():
    def take_command():
        command_taken = str('')
        try:
            with sr.Microphone() as src:
                print('listening...')
                playsound('listning_sound.wav')
                voice_taken = listener.listen(src)
                command_taken = listener.recognize_google(voice_taken)
                command_taken = command_taken.lower()
                playsound('got_it_sound.wav')
        except:
            pass
        return command_taken

    print('listening....1')
    playsound('listning_sound.wav')
    command = str('')
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                playsound('got_it_sound.wav')
                print(command)
                talk('yes....i am listening...')
                command = take_command()
            else:
                call()
    except:
        # playsound('listning_sound.wav')
        pass
    return command


def run_assistant():
    intro()
    # global run_command
    run_command = call()
    print(run_command)
    if 'play' in run_command:
        print('playing...')
        song = run_command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'what is' in run_command:
        print('question 1')
        talk('let me check the web for you')
        question = run_command.replace('what is', '')
        info = wikipedia.summary(question, 2)
        print(info)
        talk(info)
    elif 'who is ' in run_command:
        print('question 2')
        talk('let me check the web for you')
        question = run_command.replace('who is', '')
        info = wikipedia.summary(question, 1)
        print(info)
        talk(info)
    elif 'joke' in run_command:
        print('question 3')
        talk('get ready to laugh your ass off')
        joke = pyjokes.get_joke()
        talk(joke)
        talk('ha...ha...ha...ha.')
        print(joke)
    elif 'introduce your self' in run_command:
        print("introducing")
        intro()
    elif 'time' in run_command:
        print('displaying time')
        talk('your time is not correct for sure')
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is.' + time)
    elif 'thankyou' in run_command:
        print("welcome note")
        talk('you are welcome master')
        talk('you are my hero master ')
    elif 'alexa' in run_command:
        print("welcome note")
        talk('error master')
        talk('master error')
    else:
        print('sorry your kwnoledge is way beyond my reach')
        talk('sorry your kwnoledge is way beyond my reach')


while True:
    run_assistant()
