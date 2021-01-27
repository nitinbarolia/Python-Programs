import pyttsx3
friend = pyttsx3.init()
speech = input("say somthing: ")
friend.say(speech)
friend.runAndWait()
