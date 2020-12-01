import random
import pyttsx3 #speech to text


engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[1].id) #set voice

rate=engine.getProperty("rate")
engine.setProperty("rate",200)

def speak(audio): # Gives output as speech
    engine.say(audio)
    engine.runAndWait()

max_guess=5
speak("Enter number between 0 to 20")
for i in range(max_guess):
    a=int(input("Enter value:"))

    if a>20:
        print("Enter number between 0 to 20")
        speak("Enter number between 0 to 20")


    elif a==None:
        print("Enter number between 0 to 20")
        speak("Enter number between 0 to 20")


    elif a==random.randint(0,20): #for different guess chance,select different number   
        print("Your guess is right")
        print("You win")
        speak("Your guess is right")
        speak("You win")
        break
    else:
        print("Your guess is wrong")
        print("please try again")
        speak("Your guess is wrong")
        speak("please try again")

