import speech_recognition as sr
import os
import subprocess
import webbrowser

def listen_command():
    recognizer = sr.Recognizer()
    mic_index = 1  # Change this to the index of your microphone
    with sr.Microphone(device_index=mic_index) as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = recognizer.listen(source)  # Removed timeout and phrase_time_limit
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print("You said: ", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

def open_chrome_tab(url):
    webbrowser.open(url)
        
def open_app(app_path):
    subprocess.Popen([app_path])

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    open_chrome_tab(url)

if __name__ == "__main__":
    while True:
        command = listen_command()
        if "open chrome" in command:
            open_chrome_tab("https://www.google.com")
        elif "open youtube" in command:
            open_chrome_tab("https://www.youtube.com")
        elif "open chat gpt" in command:
            open_chrome_tab("https://chatgpt.com/")
        elif "open notepad" in command:
            open_app("notepad.exe")
        elif "search for" in command:
            search_query = command.replace("search for", "").strip()
            search_google(search_query)
        elif "shutdown" in command:
            os.system("shutdown /s /t 1")
        elif "restart" in command:
            os.system("shutdown /r /t 1")
        elif "exit" in command:
            break
        else:
            print("Command not recognized")

