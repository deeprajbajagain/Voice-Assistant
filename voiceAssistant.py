import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set the voice property (index 1 for female voice, 0 for male voice)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # You can change the index to 0 for a male voice

# Initialize the recognizer
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def cmd():
    with sr.Microphone() as source:
        print('Clearing background noises...Please wait')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything...')
        recorded_audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(recorded_audio)
        print(f"You said: {command}")
        
        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(f"Current time is {time}")
            speak(f"Current time is {time}")
        
        elif 'open browser' in command:
            webbrowser.open('https://www.google.com')
            speak("Opening Google Chrome")
        
        elif 'play' in command:
            song = command.replace('play', '')
            pywhatkit.playonyt(song)
            speak(f'Playing {song}')
        
        elif 'run' in command:
            app = command.replace('run', '')
            subprocess.call(app)
            speak(f'Running {app}')
        
        elif 'exit' in command or 'stop' in command:
            speak("Goodbye!")
            exit()
        
        else:
            speak("Sorry, I did not understand that.")
    
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        speak("Sorry, I did not understand that.")
    
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        speak(f"Could not request results; {e}")

if __name__ == "__main__":
    speak("How can I help you today?")
    while True:
        cmd()
