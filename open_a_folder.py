import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import time
import pyautogui

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to microphone input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

# Function to open Google Chrome with a specific URL
def open_chrome(url):
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # Path to Chrome executable
    webbrowser.get(chrome_path).open(url)


def search_song_on_youtube(song_name):
    # Open YouTube
    open_chrome("https://www.youtube.com")
    # Wait for the page to load
    time.sleep(5)
    # Press Tab 4 times to get to the search bar
    for _ in range(4):
        pyautogui.press('tab')
        time.sleep(0.5)
    # Type the song name and press Enter
    pyautogui.write(song_name)
    pyautogui.press('enter')
    speak(f"Searching for {song_name} on YouTube.")



def open_capcut():
    capcut_path = r"C:\Users\conta\AppData\Local\CapCut\Apps\CapCut.exe"  # Replace with the actual path to CapCut executable
    os.system(f'start "" "{capcut_path}"')
    speak("Opening CapCut.")

def navigate_folders():
    current_path = os.getcwd()
    
    speak(f"You are currently in {current_path}. Which folder do you want to go to?")
    
    while True:
        folder_name = listen()
        if folder_name:
            new_path = os.path.join(current_path, folder_name)
            if os.path.isdir(new_path):
                os.chdir(new_path)
                current_path = new_path
                speak(f"Moved to {current_path}.")
            else:
                speak(f"{folder_name} is not a valid folder.")
            speak("Do you want to navigate further or open this folder?")
            action = listen()
            if "open" in action:
                os.system(f'start explorer "{current_path}"')
                speak(f"Opening {current_path} in File Explorer.")
                break
            elif "exit" in action:
                speak("Exiting navigation.")
                break

# Main function
def main():
    speak("How may I help you?")
    
    while True:
        command = listen()
        
        if "open browser" in command:
            url = "https://www.google.com"  # Change the URL to the desired website
            speak("Opening Google Chrome.")
            open_chrome(url)
            break
        elif "open youtube" in command:
            url = "https://www.youtube.com"  # Open YouTube
            speak("Opening youtube")
            open_chrome(url)
            break
        elif "play a song" in command:
            speak("Which song do you want to play?")
            song_name = listen()
            search_song_on_youtube(song_name)
            break
        elif "open cap cut" in command:
            open_capcut()
            break
        elif "open folder" in command:
            navigate_folders()
        elif "exit" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
