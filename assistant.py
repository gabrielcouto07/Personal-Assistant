import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import pyjokes
import webbrowser
import tkinter as tk
from tkinter import scrolledtext

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def talk(text):
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"Assistant: {text}\n\n")
    chat_window.config(state=tk.DISABLED)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            talk("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'assistant' in command:
                command = command.replace('assistant', '')
                print(command)
                return command
    except:
        pass
    return ""

def run_assistant(command):
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'search' in command:
        search = command.replace('search', '')
        talk('Searching ' + search)
        pywhatkit.search(search)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open' in command:
        site = command.replace('open', '')
        talk('Opening ' + site)
        webbrowser.open(f'https://{site}.com')
    else:
        talk("I didn't understand that. Please try again.")

def send_message():
    user_input = user_entry.get()
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_input}\n")
    chat_window.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)
    run_assistant(user_input)

def voice_command():
    command = take_command()
    if command:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"You: {command}\n")
        chat_window.config(state=tk.DISABLED)
        run_assistant(command)
    else:
        talk("I couldn't hear you. Please try again.")

# Set up the main application window
root = tk.Tk()
root.title("Personal Assistant")

# Create a chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.config(state=tk.NORMAL)
chat_window.insert(tk.END, "Assistant: Hi! I'm your personal assistant. How can I help you today?\n\n")
chat_window.config(state=tk.DISABLED)

# Create a text entry box for user input
user_entry = tk.Entry(root, width=100)
user_entry.pack(padx=10, pady=10, fill=tk.X)

# Create a send button for text input
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=10)

# Create a button for voice commands
voice_button = tk.Button(root, text="Voice Command", command=voice_command)
voice_button.pack(pady=10)

# Run the application
root.mainloop()
