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


def intro():
    engine.say('hi i am sophie.... your personal assistant')
    engine.say('how can i help you')
    engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()

while True:

    def take_command():
        intro()
        try:
            with sr.Microphone() as source:
                print('listning...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'sophie' in command:
                    talk('yes tell me')
                    command = command.replace('sophie','')
                    print(command)
                else:
                    take_command()
        except:
            pass
        return command


    def run_shashi():
        run_command = take_command()
        print(run_command)
        if 'play' in run_command:
            print('playing...')
            song = run_command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'time' in run_command:
            print('displaying time')
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('current time is.' + time)
        elif 'what is ' in run_command:
            print('question type 1')
            question = run_command.replace('what is a', '')
            info = wikipedia.summary(question, 2)
            print(info)
            talk(info)
        elif 'how is'in run_command:
            print("question type 2")
            question = run_command.replace('how is','')
            info = wikipedia.summary(question,2)
            print(info)
            talk(info)
        elif 'who is ' in run_command:
            print('question type 3')
            question = run_command.replace('who is ', '')
            info = wikipedia.summary(question, 1)
            print(info)
            talk(info)
        elif 'joke' in run_command:
            print("gety ready to laugh")
            joke = pyjokes.get_joke()
            talk(joke)
            talk('ha..ha..ha..ha..')
        elif 'how are you' in run_command:
            talk('i am fineeeeeeeeeeee......... taaaankssssssss')
        else:
            print(run_command)
            talk('sorry i will ckeck on the web for that')
            info = wikipedia.summary(run_command, 2)
            print(info)
            talk(info)



    run_shashi()
