import pyttsx3 #Speech to text
import speech_recognition as sr  
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)
print()


def speak(audio):# Gives output as speech
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=0.5
        audio=r.listen(source)


    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"Your Turn: {query}\n")

    except Exception:
        print("say  that again please...")
        return "None"
    return query

a=["stone","paper","scissor"]
count=6
me=0
pc=0

for i in range(count):
    query=takeCommand().lower()
    c=random.choice(a)
    b=query
    print("PC turn:",c)

    if b == c:
         speak("  This time Match tie")
         if "  This time Match tie":
             pc=pc
             me=me


    elif b=="stone":
        if c=="paper":
            speak("This time I win")
            if "This time I win":
                pc+=1

        elif c=="scissor":
            speak(" This time YOU  win")
            if "This time YOU  win":
                me+=1

    elif b=="paper":
        if c=="scissor":
            speak("This time I win")
            if "This time I win":
                pc += 1
        elif c=="stone":
            speak("This time YOU win")
            if "This time YOU win":
                me += 1

    elif b=="scissor":
        if c=="stone":
            speak("This time I win")
            if "This time I win":
                pc += 1
        elif c=="paper":
            speak("This time YOU win")
            if "This time YOU win":
                me += 1

print("Your Score:",me)
print("PC Score:",pc)

if me>pc:
    speak("YOU win this match ")
elif me==pc:
    speak("this match is tie")
else:
    speak("I win this match ")