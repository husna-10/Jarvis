import pyttsx3
import speech_recognition as sr
import webbrowser
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language='en-in')
            print(f"user said:{query}")
            return query
        except Exception as e:
            return "Sorry, some error occuured"
if __name__ == "__main__":
    say("Hello, world!")
    while True:
        print('Listening...')
        query=takeCommand()
        if "Open Youtube".lower() in query.lower():
            webbrowser.open("https://www.youtube.com")
            say("opening Youtube sir")
        say(query)























import win32com.client
speaker=win32com.client.Dispatch("SAPI.SpVoice")
# while 1:
#     print("enter the text")
#     s=input()
#     speaker.speak(s)