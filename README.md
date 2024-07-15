# Voice Assistant Project

## Description
This project is a simple voice assistant application built using Python. It leverages speech recognition to understand voice commands and perform various tasks such as telling the time, opening a web browser, playing songs on YouTube, and running applications.

## Functionalities
The voice assistant can perform the following tasks:
- Tell the current time when the user asks for it.
- Open a web browser (Google Chrome).
- Play a song on YouTube.
- Run an application specified by the user.
- Exit the program when the user commands it to stop.

## Future Functionalities
Additional functionalities that can be added:
- Fetch and read the latest news headlines.
- Provide weather updates.
- Set reminders or alarms.
- Send emails or messages.
- Control smart home devices.
- Answer general knowledge questions using a web API.

## Requirements
The following Python libraries are required for this project:
- `speech_recognition`
- `datetime`
- `subprocess`
- `pywhatkit`
- `pyttsx3`
- `webbrowser`

## Installation
1. Clone the repository to your local machine.
2. Install the required libraries using `pip`:

    ```bash
    pip install SpeechRecognition
    pip install pywhatkit
    pip install pyttsx3
    ```

## Usage
1. Open your terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script:

    ```bash
    python voice_assistant.py
    ```

4. Speak your commands clearly when prompted.

## Code Explanation
```python
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
        print('Ask me anything..')
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
