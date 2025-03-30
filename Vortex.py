import speech_recognition as sr
import pyttsx3   # Library for converting text to speech
import musicLib
import webbrowser 
import requests
from openai import OpenAI

recognizer=sr.Recognizer()
engine = pyttsx3.init()
newsapi= "fd6c7f4726f34d3a9bf9bacbc28bb00f"

def speak(text):
    rate = engine.getProperty('rate')    # Changing the voice speed rate 
    print (rate)                        
    engine.setProperty('rate', 200)      # Smaller the number slower the voice speed
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male 1 for female
    engine.say(text)
    engine.runAndWait()                  # Will speak the text and then stop the program

def aiProcess(command):
    client=OpenAI(api_key="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")
    completion=client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":"You are a virtual assistant named Vortex skilled in general task like and Google"},
            {"role":"system","content":command}
        ]
    )
    return completion.choice[0].message.content

def processCommand(c):
    if "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif 'open facebook' in c.lower():
        webbrowser.open("https://facebook.com")
    elif 'open linkedin' in c.lower():
        webbrowser.open("https://linkedin.com")
    elif 'open google' in c.lower():
        webbrowser.open("https://google.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link= musicLib.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()  # Convert response to JSON

        # Extracting headlines
        articles = data.get("articles", [])  # Get list of articles
        print("Top News Headlines:\n")
        for idx, article in enumerate(articles[:], start=1):  
            speak(f"{idx}. {article['title']}")
    else:
        # Let openAi handle the requests
        output=aiProcess(c)
        speak(output)
   

if __name__=="__main__":
    speak("Initializing Vortex........")
    # Listen for the wake word "Vortex"
    # Obtain word from the microphone
    while True:
        r=sr.Recognizer()
        
        print("Recognizing....")
        # Recoginise speech through sphinx
        try:
            with sr.Microphone() as source:
                print("Say something.")
                audio=r.listen(source, timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower()=="vortex"):
                speak("Ya")
                # Listen for commands
                with sr.Microphone() as source:
                    print("Vortex active...")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
